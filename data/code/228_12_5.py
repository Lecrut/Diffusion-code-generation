import turtle

class TriangleDrawer:
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        for _ in range(3):
            self.forward()
            self.left()

    def forward(self):
        turtle.forward(self.side_length)

    def left(self):
        turtle.left(120)

if __name__ == '__main__':
    drawer = TriangleDrawer(100)
    drawer.draw()
    turtle.done()