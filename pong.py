import turtle
import winsound


window = turtle.Screen()
window.title("Pong by @colinodowd")
window.bgcolor("black")
window.setup(width = 800, height=600)

window.tracer(0) #stops window from updating, forces us to manually update (can make it go faster)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #creating a turtle object
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle() #creating a turtle object
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle() #creating a turtle object
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font =("Courier", 24, "normal"))


#Functions
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)
	
def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)
		
def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
	
def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
	
#Keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

#main game loop
while True: 
	window.update()
	
	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#Border checking
	if (ball.ycor() > 290):
		ball.sety(290)
		ball.dy *= -1 #reverses direction on ball
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	
	
	if (ball.ycor() < -290):
		ball.sety(-290)
		ball.dy *= -1 #reverses direction on ball
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	

	if (ball.xcor() > 390):
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font =("Courier", 24, "normal"))
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	

	if (ball.xcor() < -390):
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font =("Courier", 24, "normal"))
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	


	# Paddle and ball collisions 
	if ((ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 70)) and (ball.ycor() > (paddle_b.ycor() - 70))):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	


	if ((ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < (paddle_a.ycor() + 70)) and (ball.ycor() > (paddle_a.ycor() - 70))):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)	
		
