# Imports
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game state variables
is_paused = False
is_on = True

def toggle_pause():
    global is_paused
    is_paused = not is_paused

def restart_game():
    ball.reset_position()
    scoreboard.l_score = 0
    scoreboard.r_score = 0
    scoreboard.update_scoreboard()

def quit_game():
    global is_on
    is_on = False

screen.listen()
# Paddle controls
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
# Game controls
screen.onkeypress(toggle_pause, "p")
screen.onkeypress(restart_game, "r")
screen.onkeypress(quit_game, "Escape")

while is_on:
    if not is_paused:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall then bounce.
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y()

        # Detect collision with paddle then bounce.
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect R paddle misses then reset.
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle misses then reset.
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
    else:
        screen.update()
        time.sleep(0.1)  # Reduce CPU usage while paused

screen.exitonclick()
