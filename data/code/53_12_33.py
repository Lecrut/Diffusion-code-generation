import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class SquareSideCalculator:
    def __init__(self, area):
        self.area = area
    def compute_side_length(self):
        try:
            return calculate_square_side_length(self.area)
        except ValueError as e:
            print(e)
            return None

if __name__ == '__main__':
    sample_area = 49.0
    calculator = SquareSideCalculator(sample_area)
    side_length = calculator.compute_side_length()
    if side_length is not None:
        print(side_length)