import turtle
t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.speed(100)
t.color("white")
x = 1
while True:
    t.forward(x)
    t.right(60)
    t.forward(x)
    t.right(60)
    t.forward(x)
    t.right(60)
    t.forward(x)
    t.right(60)
    x += 1
    t.right(90)
    if x == 80:
        break
t.hideturtle()
turtle.done()
