from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import GameScore
import time
screen = Screen()
screen.tracer(0)



screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgpic("image/pong.png")
screen.listen()




right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball =Ball()
scoreboard = GameScore()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()



screen.exitonclick()
