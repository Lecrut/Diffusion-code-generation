import turtle

class TriangleDrawer:
    def __init__(self, side_length):
        self.side_length = side_length

    def draw_triangle(self):
        for _ in range(3):
            turtle.forward(self.side_length)
            turtle.left(120)

if __name__ == '__main__':
    drawer = TriangleDrawer(100)
    drawer.draw_triangle()
    turtle.done()