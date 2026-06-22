import math

class GeometryCalculator:
    def __init__(self):
        self.circle_radius = 5
        self.square_side_length = 4

    def calculate_circle_area(self):
        return math.pi * self.circle_radius ** 2

    def calculate_square_area(self):
        return self.square_side_length ** 2

    def calculate_total_area(self):
        circle_area = self.calculate_circle_area()
        square_area = self.calculate_square_area()
        total_area = circle_area + square_area
        return total_area

if __name__ == '__main__':
    calculator = GeometryCalculator()
    print(f"Circle Area: {calculator.calculate_circle_area()}")
    print(f"Square Area: {calculator.calculate_square_area()}")
    print(f"Total Area: {calculator.calculate_total_area()}")