import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        if base <= 0 or height <= 0 or side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All dimensions must be positive")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        circle = Circle(5)
        print("Circle Area:", circle.area())
        print("Circle Perimeter:", circle.perimeter())

        triangle = Triangle(4, 6, 7, 8, 9)
        print("Triangle Area:", triangle.area())
        print("Triangle Perimeter:", triangle.perimeter())
    except ValueError as e:
        print(e)