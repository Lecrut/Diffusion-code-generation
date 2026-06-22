import math

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = CircleAreaCalculator(5)
        print(circle.calculate_area())
    except ValueError as e:
        print(e)

    try:
        circle = CircleAreaCalculator(-3)
        print(circle.calculate_area())
    except ValueError as e:
        print(e)