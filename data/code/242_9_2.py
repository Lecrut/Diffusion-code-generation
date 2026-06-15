class Shape:
    def area(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
if __name__ == '__main__':
    circle = Circle(5)
    square = Square(4)
    circle_area = circle.area()
    square_area = square.area()
    print(f"Circle Area: {circle_area}")
    print(f"Square Area: {square_area}")