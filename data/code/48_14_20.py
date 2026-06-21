import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_sides(self):
        return self.side1, self.side2, self.side3

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_sides(self):
        return self.length, self.width, self.length, self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(6, 8)
    circle = Circle(7)

    print("Triangle sides:", triangle.get_sides())
    print("Rectangle sides:", rectangle.get_sides())
    print("Circle diameter:", circle.get_diameter())