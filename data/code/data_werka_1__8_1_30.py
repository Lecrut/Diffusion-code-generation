import math

class Shape:
    def area(self):
        return 0.0

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
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    shape_types = {
        'rectangle': Rectangle(5.0, 3.0),
        'circle': Circle(4.0)
    }

    for shape_name, shape in shape_types.items():
        print(f"The area of the {shape_name} is: {shape.area()}")