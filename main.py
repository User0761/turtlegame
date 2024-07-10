
import random
import turtle

screen=turtle.Screen()
screen.setup(400,400)
screen.bgcolor("cyan")
t = turtle.Turtle()
t.color("green")
t.shape("turtle")
t.speed(0)
screen.colormode(255)

check_points = []
for i in range(12):
  check_point = turtle.Turtle()
  check_point.speed(0)
  check_point.penup()
  check_point.color("orange")
  check_point.shape("circle")
  x = random.randint(-190,190)
  y = random.randint(-190,190)
  check_point.setposition(x,y)
  check_points.append(check_point)
def up():
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.setheading(90)
  t.forward(10)
def down():
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.setheading(270)
  t.forward(10)
def right():
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.setheading(0)
  t.forward(10)
def left():
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  t.setheading(180)
  t.forward(10)
screen.listen()
screen.onkey(up,'Up')
screen.onkey(down,'Down')
screen.onkey(right,'Right')
screen.onkey(left,'Left')
screen.mainloop()