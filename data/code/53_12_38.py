import math

def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError('Area must be a number')
    if area < 0:
        raise ValueError('Area cannot be negative')

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

class SquareSideLengthCalculator:

    def __init__(self, area):
        self.area = area

    def compute(self):
        return calculate_square_side_length(self.area)
if __name__ == '__main__':
    sample_areas = [16.0, 25.0, 36.0, -4.0]
    for area in sample_areas:
        try:
            calculator = SquareSideLengthCalculator(area)
            side_length = calculator.compute()
            print(f'Side length of square with area {area}: {side_length}')
        except (ValueError, TypeError) as e:
            print(f'Error calculating side length for area {area}: {e}')