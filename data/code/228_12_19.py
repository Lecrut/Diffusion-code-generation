import turtle

class TriangleDrawer:
    SIDE_LENGTH = 100

    @staticmethod
    def draw_triangle():
        for _ in range(3):
            turtle.forward(TriangleDrawer.SIDE_LENGTH)
            turtle.left(120)

if __name__ == '__main__':
    turtle.speed(1)
    TriangleDrawer.draw_triangle()
    turtle.done()