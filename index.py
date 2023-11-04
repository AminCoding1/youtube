import turtle as t
import colorsys
t.bgcolor("black")
t.speed(50)
t.pensize(1)
color=["green","orange","white","magenta"]
for i in range(200):
    t.pencolor(color[i%4])
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
t.done()