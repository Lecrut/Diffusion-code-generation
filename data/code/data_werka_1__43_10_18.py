class SquareAreaCalculator:
    MIN_VALID_SIDE_LENGTH = 0

    @staticmethod
    def validate_side_length(side_length):
        if side_length <= SquareAreaCalculator.MIN_VALID_SIDE_LENGTH:
            raise ValueError("Side length must be positive.")

    def __init__(self, side_length):
        SquareAreaCalculator.validate_side_length(side_length)
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    test_cases = [5, -3, "invalid", None]
    for value in test_cases:
        try:
            if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                side_length = float(value)
            else:
                side_length = value
            calculator = SquareAreaCalculator(side_length)
            area = calculator.calculate_area()
            print(f"Side length: {side_length}")
            print(f"Area of square: {area}\n")
        except ValueError as e:
            print(f"Error calculating area for input '{value}': {e}")