class SquareAreaCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def compute_area(self):
        return self.side_length * self.side_length

    def get_side(self):
        return self.side_length

if __name__ == '__main__':
    calculator = SquareAreaCalculator(7)
    print(calculator.get_side())
    print(calculator.compute_area())