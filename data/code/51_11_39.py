import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle1 = Circle(radius=3)
    print(circle1.perimeter())

    circle2 = Circle(radius=8.5)
    print(circle2.perimeter())