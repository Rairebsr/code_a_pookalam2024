import turtle


screen = turtle.Screen()
screen.title("Turtle Graphic")


t = turtle.Turtle()
t.speed(0)

def petal(length, col):
    t.color(col)
    t.begin_fill()
    for i in range(9):
        t.forward(length)
        t.circle(length / 4, 208)
        t.forward(length)
        t.right(180)
        t.right(-17)
    t.end_fill()

def draw_petal(t, radius,col):
    t.width(3)
    t.color(col)
    t.begin_fill()
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
    t.end_fill()

def draw_outer_circle(radius, col):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.color(col)
    t.circle(radius)
    


def large_petals_behind_circle(num_petals=8, length=150, color="violet"):
    for i in range(num_petals):
        t.color(color)
        t.begin_fill()
        t.penup()
        angle = 360 / num_petals * i
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(100)
        t.right(90)
        t.pendown()
        t.begin_fill()
        t.circle(length, 60)
        t.left(120)
        t.circle(length / 2, 60)
        t.end_fill()
        t.penup()


def large_petals(num_petals=8, length=150, color="violet"):
    for i in range(num_petals):
        t.color(color)
        t.width(5)
        t.penup()
        angle = 360 / num_petals * i
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(100)
        t.right(90)
        t.pendown()
        t.circle(length, 60)
        t.left(120)
        t.circle(length / 2, 60)
        t.penup()



def pos():
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()


t.width(5)
draw_outer_circle(300,"#7c06b8")
draw_outer_circle(305,"white")
draw_outer_circle(310,"#7c06b8")
t.width(50)
draw_outer_circle(270,"#248017")
draw_outer_circle(220,"#a10909")
pos()
for _ in range(8):
    draw_petal(t, 300,"#fe082a")
    t.right(360 / 8)

t.left(85)
t.penup()
t.pendown()

petal(250, "#ff6619")
petal(230, "orange")
petal(210, "yellow")

large_petals_behind_circle(num_petals=20, length=150, color="dark red")
large_petals_behind_circle(num_petals=20, length=130, color="crimson")
large_petals_behind_circle(num_petals=20, length=120, color="orange")
large_petals(num_petals=40, length=120, color="white")

pos()


for _ in range(18):
    draw_petal(t, 100,"#a10909")
    t.right(360 / 18)
    
t.right(50)
t.penup()
t.pendown()
    
for _ in range(18):
    draw_petal(t, 90,"#df2c04")
    t.right(360 / 18)
    
t.right(50)
t.penup()
t.pendown()

for _ in range(18):
    draw_petal(t, 80,"#ff5009")
    t.right(360 / 18)

t.right(50)
t.penup()
t.pendown()

for _ in range(18):
    draw_petal(t, 70,"#ff6609")
    t.right(360 / 18)
    
t.right(50)
t.penup()
t.pendown()

for _ in range(18):
    draw_petal(t, 60,"#D2042D")
    t.right(360 / 18)
    
t.right(50)
t.penup()
t.pendown()

for _ in range(18):
    draw_petal(t, 50,"#fff406")
    t.right(360 / 18)
    

    
pos()
def vallam():
    t.color("black")
    t.begin_fill()
    t.bk(40)
    t.setheading(90)
    t.circle(20,90)
    t.rt(180)
    t.fd(25)
    t.fd(50)
    t.circle(20,90)
    t.rt(180)
    t.fd(40)
    t.rt(90)
    t.fd(40)
    t.rt(60)
    t.fd(70)
    t.bk(100)
    t.end_fill()
    t.fd(15)
vallam()
screen.mainloop()
