import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self._validate_radius(radius)
        self._radius = radius

    @staticmethod
    def _validate_radius(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return self.PI * self._radius ** 2

if __name__ == '__main__':
    sample_radius = 4.0
    circle = Circle(sample_radius)
    print(circle.area())