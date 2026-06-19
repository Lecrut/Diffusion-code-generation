import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    circle = Circle(radius=5)
    square = Square(side_length=10)

    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())