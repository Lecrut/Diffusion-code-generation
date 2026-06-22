import math

class AreaCalculator:
    def __init__(self):
        self.circle_radius = 5
        self.square_side_length = 4

    def calculate_circle_area(self):
        return math.pi * self.circle_radius ** 2

    def calculate_square_area(self):
        return self.square_side_length ** 2

    def total_area(self):
        circle_area = self.calculate_circle_area()
        square_area = self.calculate_square_area()
        return circle_area + square_area

if __name__ == '__main__':
    calculator = AreaCalculator()
    print(calculator.total_area())