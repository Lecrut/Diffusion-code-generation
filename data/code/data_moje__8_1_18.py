import math

PI = 3.141592653589793

class Shape:
    def get_area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return PI * (self.r ** 2)

if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.get_area())
    circ = Circle(4)
    print(circ.get_area())