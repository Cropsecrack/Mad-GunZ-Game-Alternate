import turtle
screen = turtle.Screen()
screen.title("Move the Turtle!")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

t = turtle.Turtle()
t.color("cyan")
t.hideturtle()
t.penup()
t.speed(0)
t.pensize(2)

pen = turtle.Turtle()
pen.color("cyan")
pen.hideturtle()
pen.pensize(2)
pen.speed(0)
pen.pendown()

SPEED = 5

keys = {"Up": False, "Down": False, "Left": False, "Right": False}
def key_press(key):
    keys[key] = True
def key_release(key):
    keys[key] = False
screen.listen()
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeypress(lambda: key_press("Left"), "Left")
screen.onkeypress(lambda: key_press("Right"), "Right")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Left"), "Left")
screen.onkeyrelease(lambda: key_release("Right"), "Right")

def toggle_pen():
    if pen.isdown():
        pen.penup()
    else:
        pen.pendown()

def clear_screen():
    pen.clear()
    t.goto(0, 0)  
    pen.goto(0, 0) 

screen.onkey(toggle_pen, "space")
screen.onkey(clear_screen, "c")

def game_loop():
    if keys["Up"]:
        t.setheading(90)
        t.forward(SPEED)
        pen.goto(t.pos())
    if keys["Down"]:
        t.setheading(270)
        t.forward(SPEED)
        pen.goto(t.pos())
    if keys["Left"]:
        t.setheading(180)
        t.forward(SPEED)
        pen.goto(t.pos())
    if keys["Right"]:
        t.setheading(0)
        t.forward(SPEED)
        pen.goto(t.pos())

    if t.xcor() > 300 or t.xcor() < -300 or t.ycor() > 300 or t.ycor() < -300:
        t.goto(0, 0)  
        pen.penup()   
        pen.goto(0, 0)
        pen.pendown()

    
    t.clear()
    t.write("Mad GunZ", align="center", font=("Arial", 14, "bold"))

    screen.update()
    screen.ontimer(game_loop, 16)


game_loop()
turtle.done()
