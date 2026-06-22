import turtle

class BoxDrawer:
    def __init__(self, side_length):
        self.side_length = side_length
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
    
    def draw_box(self):
        for _ in range(4):
            self.turtle.forward(self.side_length)
            self.turtle.left(90)
    
    def center_box(self):
        self.turtle.penup()
        self.turtle.goto(-self.side_length / 2, self.side_length / 2)
        self.turtle.pendown()

if __name__ == '__main__':
    drawer = BoxDrawer(100)
    drawer.center_box()
    drawer.draw_box()
    turtle.done()