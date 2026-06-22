import math

class ShapeCalculator:
    def __init__(self, radius, side_length):
        self.radius = radius
        self.side_length = side_length

    def calculate_circle_circumference(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * math.pi * self.radius

    def calculate_square_perimeter(self):
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")
        return 4 * self.side_length

    def get_results(self):
        circle_circumference = self.calculate_circle_circumference()
        square_perimeter = self.calculate_square_perimeter()
        return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    try:
        sample_radius = 5.0
        sample_side_length = 4.0
        calculator = ShapeCalculator(sample_radius, sample_side_length)
        results = calculator.get_results()
        print(results)
    except ValueError as e:
        print(e)