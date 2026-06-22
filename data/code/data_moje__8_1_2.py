import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

if __name__ == '__main__':
    rect = Rectangle(4, 5)
    circ = Circle(3)
    print(rect.area())
    print(circ.area())