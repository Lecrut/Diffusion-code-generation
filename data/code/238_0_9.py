import turtle

class BoxDrawer:
    SIDE_LENGTH = 100
    COLOR = "black"

    @staticmethod
    def draw_box():
        turtle.penup()
        turtle.goto(-BoxDrawer.SIDE_LENGTH / 2, BoxDrawer.SIDE_LENGTH / 2)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(BoxDrawer.SIDE_LENGTH)
            turtle.right(90)

if __name__ == '__main__':
    BoxDrawer.draw_box()
    turtle.done()