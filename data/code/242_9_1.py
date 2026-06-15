class Shape:
    def area(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
if __name__ == '__main__':
    circle = Circle(5)
    square = Square(4)
    circle_area = circle.area()
    square_area = square.area()
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")