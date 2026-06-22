import math

class ShapeCalculator:
    PI = math.pi
    SQUARE_MULTIPLIER = 4

    @staticmethod
    def calculate_circle_circumference(radius):
        return 2 * ShapeCalculator.PI * radius

    @staticmethod
    def calculate_square_perimeter(side_length):
        return ShapeCalculator.SQUARE_MULTIPLIER * side_length

    @staticmethod
    def calculate_shapes(radius, side_length):
        circle_circumference = ShapeCalculator.calculate_circle_circumference(radius)
        square_perimeter = ShapeCalculator.calculate_square_perimeter(side_length)
        return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_radius = 6.0
    sample_side_length = 8.0
    result = ShapeCalculator.calculate_shapes(sample_radius, sample_side_length)
    print(result)