import math

PI_CONSTANT = math.pi

class Shape:
    def calculate_area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def calculate_area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return PI_CONSTANT * (self.r ** 2)

if __name__ == '__main__':
    r = Rectangle(10, 5)
    c = Circle(7)
    print(r.calculate_area())
    print(c.calculate_area())