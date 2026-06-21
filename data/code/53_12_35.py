import math
NEGATIVE_AREA_THRESHOLD = 0.0

def calculate_square_side_length(area):
    if area < NEGATIVE_AREA_THRESHOLD:
        raise ValueError('Area cannot be negative')
    return math.sqrt(area)

class SquareSideLengthCalculator:

    def __init__(self, area):
        self.area = area

    def compute_side_length(self):
        return calculate_square_side_length(self.area)
if __name__ == '__main__':
    sample_area = 49.0
    try:
        calculator = SquareSideLengthCalculator(sample_area)
        side_length = calculator.compute_side_length()
        print(side_length)
    except ValueError as e:
        print(e)