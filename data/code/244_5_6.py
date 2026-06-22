import math

class AreaCalculator:
    def __init__(self):
        self.semicircle_radius = 4
        self.rectangle_length = 5
        self.rectangle_width = 8

    def calculate_semicircle_area(self):
        return 0.5 * math.pi * (self.semicircle_radius ** 2)

    def calculate_rectangle_area(self):
        return self.rectangle_length * self.rectangle_width

    def total_area(self):
        semicircle_area = self.calculate_semicircle_area()
        rectangle_area = self.calculate_rectangle_area()
        return semicircle_area + rectangle_area

if __name__ == '__main__':
    calculator = AreaCalculator()
    print(calculator.total_area())