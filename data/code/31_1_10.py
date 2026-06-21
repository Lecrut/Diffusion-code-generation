class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def compute_square(self):
        return self.side_length ** 2

    def get_side(self):
        return self.side_length

if __name__ == '__main__':
    calculator = SquareCalculator(7)
    print(calculator.get_side())
    print(calculator.compute_square())