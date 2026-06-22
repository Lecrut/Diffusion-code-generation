import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class SquareCalculator:
    def __init__(self, area):
        self.area = area
    
    def get_side_length(self):
        try:
            return calculate_square_side_length(self.area)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_area = 25.0
    calculator = SquareCalculator(sample_area)
    side_length = calculator.get_side_length()
    print(side_length)