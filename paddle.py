from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)