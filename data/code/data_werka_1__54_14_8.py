import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(10.0)
        print(f"Area: {circle.area()}")
        print(f"Circumference: {circle.circumference()}")
    except ValueError as e:
        print(e)