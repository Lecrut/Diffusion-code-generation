import math

class Shape:
    def compute_area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def compute_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def compute_area(self):
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    rect = Rectangle(4.0, 5.0)
    circ = Circle(3.0)
    print(rect.compute_area())
    print(circ.compute_area())