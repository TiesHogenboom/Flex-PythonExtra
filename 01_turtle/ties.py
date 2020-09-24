import turtle             
my_wn = turtle.Screen()
turtle.speed(100)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.fillcolor("white")
turtle.begin_fill()

for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-10*i)
   turtle.circle(-5*i)
   turtle.circle(10*i)
   turtle.left(i)


turtle.end_fill()
turtle.done()