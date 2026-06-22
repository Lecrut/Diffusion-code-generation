import math

class CircleCalculator:
    DEFAULT_RADIUS = 5

    def __init__(self, radius=None):
        self.radius = radius if radius is not None else self.DEFAULT_RADIUS

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_calculator = CircleCalculator()
    print("Area:", circle_calculator.calculate_area())
    print("Circumference:", circle_calculator.circumference())