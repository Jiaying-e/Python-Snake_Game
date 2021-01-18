from turtle import Turtle

START_POSITIONS = [(-20, 0), (0, 0), (20, 0)]
MOVE_DISTANCE = 20
caspar = Turtle(shape="turtle")
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.caspar_body = []
        self.create_snake()
        self.head = self.caspar_body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            caspar = Turtle(shape="turtle")
            caspar.color("white")
            caspar.penup()
            caspar.goto(position)
            self.caspar_body.append(caspar)

    def move(self):
        for cas_num in range(len(self.caspar_body) - 1, 0, -1):
            new_x = self.caspar_body[cas_num - 1].xcor()
            new_y = self.caspar_body[cas_num - 1].ycor()
            self.caspar_body[cas_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)