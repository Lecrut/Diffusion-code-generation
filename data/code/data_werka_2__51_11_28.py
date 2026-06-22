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

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(radius=8.5)
        print(circle.perimeter())
    except ValueError as e:
        print(e)