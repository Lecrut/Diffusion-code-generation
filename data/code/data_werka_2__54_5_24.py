import math

class Circle:
    def __init__(self, radius):
        self._validate_radius(radius)
        self.radius = radius

    def _validate_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(7)
        print("Area:", circle.area())
        print("Circumference:", circle.circumference())
    except ValueError as e:
        print(e)