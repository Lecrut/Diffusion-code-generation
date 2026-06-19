import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height, side1=None, side2=None):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        if self.side1 and self.side2:
            return self.base + self.side1 + self.side2
        else:
            raise ValueError("Both sides of the triangle must be provided for perimeter calculation.")

if __name__ == '__main__':
    circle = Circle(radius=5)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    triangle = Triangle(base=4, height=3, side1=5, side2=6)
    print("Triangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())