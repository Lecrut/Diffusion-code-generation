import math

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
        return math.pi * self.radius * self.radius

def calculate_and_display_shapes(shapes):
    for shape in shapes:
        result = shape.area()
        print(result)

if __name__ == '__main__':
    rect = Rectangle(6, 9)
    circ = Circle(4)
    shapes_list = [rect, circ]
    calculate_and_display_shapes(shapes_list)