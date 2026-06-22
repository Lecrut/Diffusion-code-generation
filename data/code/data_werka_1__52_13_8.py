import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 8
    try:
        circle = Circle(sample_radius)
        print("Area:", circle.area())
        print("Circumference:", circle.circumference())
    except ValueError as e:
        print(e)