import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(10.5, 5.0)
    circle = Circle(4.0)

    print("Rectangle Area:", rect.area())
    print("Circle Area:", circle.area())