import math

class TriangleCalculator:
    SQRT_3 = math.sqrt(3)

    @staticmethod
    def calculate_side_length(height):
        if height <= 0:
            raise ValueError("Height must be positive")
        return (2 * height) / TriangleCalculator.SQRT_3

    @staticmethod
    def calculate_perimeter(side_length):
        return 3 * side_length

if __name__ == '__main__':
    try:
        height = 8.73
        side_length = TriangleCalculator.calculate_side_length(height)
        perimeter = TriangleCalculator.calculate_perimeter(side_length)
        print(f'Side Length: {side_length}')
        print(f'Perimeter: {perimeter}')
    except ValueError as e:
        print(e)