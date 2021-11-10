import turtle
import random

habib = turtle.Turtle()
habib.shape("turtle")

turtle.colormode(255)
distance = 0

for i in range(100):
        habib.fillcolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        habib.pu()
        habib.fd(distance)
        habib.stamp()
        habib.rt(25)
        distance += 5
        print(i)
