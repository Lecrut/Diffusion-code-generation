import math

class Shape:
    def calculate_area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.calculate_area())
    circ = Circle(7)
    print(circ.calculate_area())