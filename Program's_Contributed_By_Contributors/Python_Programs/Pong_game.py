import turtle as t
import os

player_a_score = 0
player_b_score = 0

# Create a window and set it up
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Create the right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Create the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Create a pen for the score display
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))

# Function to move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Function to move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Function to move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Function to move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Bind keys for paddle movement
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24, "normal"))
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("blue")
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")
