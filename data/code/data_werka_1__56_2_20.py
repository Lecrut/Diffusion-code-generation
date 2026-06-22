import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:

    def __init__(self, base, height, side1=None, side2=None, side3=None):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        if self.side1 is not None and self.side2 is not None and (self.side3 is not None):
            return self.side1 + self.side2 + self.side3
        else:
            raise ValueError('All sides must be provided to calculate the perimeter of a triangle.')
if __name__ == '__main__':
    circle_radius = 7.0
    circle = Circle(circle_radius)
    print(f'Circle Area: {circle.area()}')
    print(f'Circle Perimeter: {circle.perimeter()}')
    triangle_base = 10.0
    triangle_height = 5.0
    triangle_side1 = 8.0
    triangle_side2 = 6.0
    triangle_side3 = 10.0
    triangle = Triangle(triangle_base, triangle_height, triangle_side1, triangle_side2, triangle_side3)
    print(f'Triangle Area: {triangle.area()}')
    print(f'Triangle Perimeter: {triangle.perimeter()}')