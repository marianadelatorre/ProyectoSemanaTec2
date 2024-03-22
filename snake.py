"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

#Le agregue que importe choice 
from random import randrange, choice

from turtle import *

from freegames import square, vector

#aqui estan los colores que puede usar, sin incluir el rojo 
colors = ['blue', 'green', 'yellow', 'orange', 'purple']
snake_color = choice(colors)
colors.remove(snake_color)
food_color = choice(colors)

food = vector(0, 0)
food_direction = vector(0, -10) 
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
#Aqui se puso snake_color y food_color para que tome el color que se asigno arriba
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

#Se creó la función para mover la comida sin que se salga de los límites asi como detalles más específicos

def move_food():
    """Move food one step at a time."""
    global food_direction  # Utilizamos la dirección de la comida globalmente

    next_food_pos = food + food_direction 

    
    if -200 < next_food_pos.x < 190 and -200 < next_food_pos.y < 190:
        food.x = next_food_pos.x
        food.y = next_food_pos.y
    else:
        
        food_direction = vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10)

    ontimer(move_food, 1000)  


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food() 
done()

