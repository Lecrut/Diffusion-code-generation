import turtle

class TriangleDrawer:
    def __init__(self):
        self.turtle = turtle.Turtle()
    
    def draw_triangle(self, side_length):
        for _ in range(3):
            self.turtle.forward(side_length)
            self.turtle.left(120)

if __name__ == '__main__':
    drawer = TriangleDrawer()
    drawer.draw_triangle(100)
    turtle.done()