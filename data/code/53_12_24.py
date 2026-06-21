import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class SquareCalculator:
    def __init__(self, area):
        self.area = area

    def get_side_length(self):
        return calculate_square_side_length(self.area)

if __name__ == '__main__':
    sample_area = 36.0
    try:
        calculator = SquareCalculator(sample_area)
        side_length = calculator.get_side_length()
        print(side_length)
    except ValueError as e:
        print(e)