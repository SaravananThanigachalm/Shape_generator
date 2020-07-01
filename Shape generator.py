# -*- coding: utf-8 -*-
"""
Welcome to the Shape generator V1

@author: Saravanan T

last edited date - 1/7/2020
"""
import random
import turtle

screen = turtle.Screen()
screen.setup(1024, 720)
turtle.color('red')
style1 = ('Arial', 30, 'italic')
turtle.write('Welcome to Shape Generator V1', font=style1, align='center')
turtle.hideturtle()


class Polygon:
    color = ["red","yellow", "gold", "orange", "maroon", "violet", "magenta", "navy blue", "skyblue", "lightgreen", "green", "darkgreen", "brown", "gray"]
    picked_color = random.choice(color)
    def __init__(self, name, sides, length, color = picked_color):
        self.name = name
        self.sides = sides
        self.length = length
        self.color = color
        self.interior = (self.sides - 2) * 180
        self.angles = self.interior / self.sides
        
        
    def draw(self):
        turtle.pencolor(self.color)
        turtle.pensize(self.length/6)
        for i in range(self.sides):
            turtle.forward(self.length)
            turtle.right(180 - self.angles)
        turtle.done()



x = str(input("Please specify name of the Polygon"))
y = int(input("Please specify the number of sides"))
z = int(input("Please specify the length of the side"))

x = Polygon(x, y, z)
x.draw()

""" The code is still under developement, there are few bugs, if an error pops-up please run twice and the code will run 
thank you """