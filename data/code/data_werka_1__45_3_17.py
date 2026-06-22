import math

def validate_positive_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")

class CircleAreaCalculator:
    def __init__(self, radius):
        validate_positive_radius(radius)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        validate_positive_radius(value)
        self._radius = value

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = CircleAreaCalculator(7.0)
        print(circle.calculate_area())
    except ValueError as e:
        print(e)