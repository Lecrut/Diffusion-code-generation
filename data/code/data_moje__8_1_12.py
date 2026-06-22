import math

class Shape:
    def calculate_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    print(rect.calculate_area())
    circ = Circle(3)
    print(circ.calculate_area())