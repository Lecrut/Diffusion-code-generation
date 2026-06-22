import turtle

class DrawingCanvas:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Black Square")
        self.turtle = turtle.Turtle()

    def draw_square(self, side_length=100, color="black"):
        self.turtle.fillcolor(color)
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(side_length)
            self.turtle.left(90)
        self.turtle.end_fill()

if __name__ == '__main__':
    canvas = DrawingCanvas()
    canvas.draw_square()
    turtle.done()