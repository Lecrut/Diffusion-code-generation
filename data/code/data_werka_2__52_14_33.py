def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length
        self.validate_side_length()

    def validate_side_length(self):
        if not isinstance(self.side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")

    def get_area(self):
        return calculate_square_area(self.side_length)

if __name__ == '__main__':
    sample_side_lengths = [4, 6]
    for side_length in sample_side_lengths:
        calculator = SquareCalculator(side_length)
        area = calculator.get_area()
        print(area)