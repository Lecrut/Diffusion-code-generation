import math

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_sides(self):
        return (self.side1, self.side2, self.side3)

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_sides(self):
        return (self.length, self.width, self.length, self.width)

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

def measure_shapes():
    triangle_sides = (3, 4, 5)
    rectangle_dimensions = (6, 8)
    circle_radius = 7
    triangle = Triangle(*triangle_sides)
    rectangle = Rectangle(*rectangle_dimensions)
    circle = Circle(circle_radius)
    print('Triangle Sides:', triangle.get_sides())
    print('Rectangle Sides:', rectangle.get_sides())
    print('Circle Diameter:', circle.get_diameter())
if __name__ == '__main__':
    measure_shapes()