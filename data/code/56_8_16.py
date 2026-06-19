import math

class ShapeCalculator:
    def __init__(self, circle_radius, square_side):
        self.circle_radius = circle_radius
        self.square_side = square_side

    def calculate_circle_circumference(self):
        return 2 * math.pi * self.circle_radius

    def calculate_square_perimeter(self):
        return 4 * self.square_side

    def get_results(self):
        circumference = self.calculate_circle_circumference()
        perimeter = self.calculate_square_perimeter()
        return (circumference, perimeter)

if __name__ == '__main__':
    sample_radius = 6.0
    sample_side_length = 8.0
    calculator = ShapeCalculator(sample_radius, sample_side_length)
    print("Circumference:", calculator.calculate_circle_circumference())
    print("Perimeter:", calculator.calculate_square_perimeter())
    print("Results Tuple:", calculator.get_results())