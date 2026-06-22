import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def validate_radius(self):
        if self.radius <= 0:
            raise ValueError('Radius must be positive')

    def area(self):
        self.validate_radius()
        return math.pi * self.radius ** 2

    def perimeter(self):
        self.validate_radius()
        return 2 * math.pi * self.radius

class Triangle:

    def __init__(self, base, height, side1=None, side2=None, side3=None):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def validate_triangle(self):
        if self.height <= 0 or self.base <= 0:
            raise ValueError('Base and height must be positive')
        if self.side1 is not None and (self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0):
            raise ValueError('Sides must be positive')

    def area(self):
        self.validate_triangle()
        return 0.5 * self.base * self.height

    def perimeter(self):
        self.validate_triangle()
        if self.side1 is not None:
            return self.side1 + self.side2 + self.side3
        else:
            raise ValueError('Perimeter calculation requires all sides to be specified')
if __name__ == '__main__':
    circle = Circle(5)
    triangle = Triangle(base=6, height=4, side1=5, side2=5, side3=8)
    print('Circle Area:', circle.area())
    print('Circle Perimeter:', circle.perimeter())
    print('Triangle Area:', triangle.area())
    print('Triangle Perimeter:', triangle.perimeter())