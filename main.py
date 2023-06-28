import turtle
import random

draw_board=turtle.Screen()
draw_board.bgcolor("light pink")
draw_board.title("interactive board")
FONT=("Arial",20,"normal")
score=0
game_over=False
#turtle list

turtle_list=[]
countturtle=turtle.Turtle()
score_turtle=turtle.Turtle()
def  scoresetup():
    #score
    topheight=draw_board.window_height()
    y=topheight*0.45


    score_turtle.penup()

    score_turtle.setpos(0,y)

    score_turtle.write(arg="SCORE: 0",move=False,align="center", font=FONT)

    score_turtle.hideturtle()

def make_turtle(x,y):
    myturt=turtle.Turtle()

    def handle_click(x,y):
        global score

        score+=1
        score_turtle.clear()
        score_turtle.write(arg="SCORE: {}".format(score), move=False, align="center", font=FONT)

       # print(x,y)

    myturt.onclick(handle_click)
    myturt.penup()
    myturt.shape("turtle")
    myturt.shapesize(2,2)
    myturt.setpos(x*10,y*10)
    turtle_list.append(myturt)

xcoord=[-20,-10,0,10,20]
ycoord=[20,10,0,-10]

def setupturtle():

    for i in xcoord:
        for j in ycoord:
            make_turtle(i,j)
def hide_turtle():
    for t in turtle_list:
        t.hideturtle()

def showrandomly():
    if not game_over:


        random.choice(turtle_list).showturtle()
        draw_board.ontimer(showrandomly,1200)
        hide_turtle()

def countdown(time):
    global game_over
    countturtle.hideturtle()
    topheight = draw_board.window_height()
    y = topheight * 0.35

    countturtle.penup()

    countturtle.setpos(0, y)
    if time > 0:
        countturtle.clear()
        countturtle.write(arg=f"TIME :{time}", move=False, align="center", font=FONT)
        draw_board.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over=True
        countturtle.clear()
        hide_turtle()
        countturtle.write(arg="GAME OVER",move= False, align="center",font=FONT)


scoresetup()
turtle.tracer(0)

setupturtle()
hide_turtle()
showrandomly()
countdown(10)
turtle.tracer(1)
"""""
def turtforw():
    myturt.forward(30)

def rotateangle():
   # myturt.right(10)
    myturt.setheading(myturt.heading()+10)

def clearscreen():
    myturt.clear()

def returnhome():
    myturt.home()

def pen_up():
    myturt.penup()

def pen_down():
    myturt.pendown()
""""""""
""""""
draw_board.listen()
draw_board.onkey(fun=turtforw,key="d")
draw_board.onkey(fun=rotateangle,key="space")
draw_board.onkey(fun=clearscreen,key="c")
draw_board.onkey(fun=returnhome,key="h")
draw_board.onkey(fun=pen_up,key="u")
draw_board.onkey(fun=pen_down,key="q")
"""""""""
turtle.mainloop()