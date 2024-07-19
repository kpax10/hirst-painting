from turtle import *
import turtle
import random


def place_dot():
    tim.pencolor(random.choice(color_list))
    tim.pendown()
    tim.dot(dot_size)
    tim.penup()
    tim.forward(dot_space)


def new_line():
    x_cor = tim.xcor()
    y_cor = tim.ycor()
    tim.teleport(x_cor - 500, y_cor + 50)


color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37)]
x_pos = -250
y_pos = -250
dot_size = 20
dot_space = 50


turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')
tim.setx(x_pos)
tim.sety(y_pos)

for _ in range(10):
    for _ in range(10):
        place_dot()
    new_line()

screen = Screen()
screen.exitonclick()
