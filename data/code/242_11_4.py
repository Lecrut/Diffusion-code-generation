import math
class Shape:
    def calculate_area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side ** 2
if __name__ == '__main__':
    circle = Circle(5)
    square = Square(4)
    circle_area = circle.calculate_area()
    square_area = square.calculate_area()
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    if circle_area > square_area:
        print("The circle has a larger area.")
    elif square_area > circle_area:
        print("The square has a larger area.")
    else:
        print("The areas are equal.")