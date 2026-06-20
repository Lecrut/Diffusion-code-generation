import math

_BASE_AREA = 0

class Shape:
    def get_area(self):
        return _BASE_AREA

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    circ = Circle(3)
    print(rect.get_area())
    print(circ.get_area())