import math

class SquareCalculator:
    MIN_AREA = 0

    @staticmethod
    def calculate_side_length(area):
        if area < SquareCalculator.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [16, 25, 81]
    for area in sample_areas:
        side_length = SquareCalculator.calculate_side_length(area)
        print(side_length)