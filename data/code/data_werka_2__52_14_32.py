def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a number")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

class SquareAreaCalculator:
    def __init__(self, side_length):
        self.side_length = side_length
        validate_side_length(self.side_length)

    def get_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 4
    area_direct = calculate_square_area(sample_side_length)
    print(area_direct)

    calculator = SquareAreaCalculator(sample_side_length)
    area_calculator = calculator.get_area()
    print(area_calculator)