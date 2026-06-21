class SquareAreaCalculator:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def get_side(self):
        return self.side

if __name__ == '__main__':
    calculator = SquareAreaCalculator(50)
    print(calculator.calculate_area())
    print(calculator.get_side())