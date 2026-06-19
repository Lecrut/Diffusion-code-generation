class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        if self.side_length <= 0:
            raise ValueError("Side length must be positive")
        return 4 * self.side_length

if __name__ == '__main__':
    calculator = SquareCalculator(8)
    try:
        perimeter = calculator.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)