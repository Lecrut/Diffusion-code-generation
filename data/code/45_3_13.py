import math

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not self.is_valid_radius(value):
            raise ValueError("Radius must be positive")
        self._radius = value

    def is_valid_radius(self, value):
        return value > 0

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = CircleAreaCalculator(5.0)
        print(circle.calculate_area())
    except ValueError as e:
        print(e)