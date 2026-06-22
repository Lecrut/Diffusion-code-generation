import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height if self.width > 0 and self.height > 0 else 0.0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2) if self.radius > 0 else 0.0

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    circle = Circle(4.0)

    print(f"Rectangle Area: {rect.area()}")
    print(f"Circle Area: {circle.area()}")