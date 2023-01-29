import turtle

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.speed(("fastest"))
tim.penup()
tim.hideturtle()
turtle.colormode(255)
tim.pencolor("white")
tim.setposition(-250, -200)
position = tim.position
increase_y = 50


def new_position(y_position):
    tim.setposition(-250, -200 + y_position)
    return 50

def draw_dot():
    for _ in range(10):
        tuple = random.choice(color_list)
        tim.dot(20, tuple)
        tim.forward(50)


for _ in range(10):
    draw_dot()
    increase_y += new_position(increase_y)













screen = Screen()
screen.canvwidth = 500
screen.canvheight = 500
screen.exitonclick()



