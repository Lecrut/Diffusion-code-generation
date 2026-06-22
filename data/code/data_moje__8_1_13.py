import math

PI = math.pi

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * (self.radius * self.radius)

def format_output(shape, name):
    return f"{name} Area: {shape.area()}"

if __name__ == '__main__':
    rect = Rectangle(8, 12)
    circ = Circle(10)
    print(format_output(rect, "Rectangle"))
    print(format_output(circ, "Circle"))