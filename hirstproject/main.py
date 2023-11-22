###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Turtle, Screen
import turtle as t
import random
tem = t.Turtle()
t.colormode(255)
tem.penup()
tem.hideturtle()
tem.speed("fastest")
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tem.right(140)
tem.forward(350)
tem.setheading(0)

for _ in range(1, 151):
    tem.dot(35, random.choice(color_list))
    tem.forward(50)
    if _%10 == 0:
        

        tem.left(90)
        tem.forward(60)
        tem.left(90)
        tem.forward(500)
        tem.setheading(0)




























screen = Screen()
screen.exitonclick()
