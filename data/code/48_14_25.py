import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def sides(self):
        return (self.side1, self.side2, self.side3)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def sides(self):
        return (self.length, self.width, self.length, self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def sides(self):
        return (2 * math.pi * self.radius,)

def measure_shapes(shapes):
    results = {}
    for shape in shapes:
        results[type(shape).__name__] = shape.sides()
    return results

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(6, 8)
    circle = Circle(7)

    shapes = [triangle, rectangle, circle]
    measurements = measure_shapes(shapes)

    for shape_name, sides in measurements.items():
        print(f"{shape_name} sides: {sides}")