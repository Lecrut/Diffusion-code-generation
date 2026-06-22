class SquareAreaCalculator:

    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2
if __name__ == '__main__':
    calculator1 = SquareAreaCalculator(5)
    print(calculator1.calculate_area())
    calculator2 = SquareAreaCalculator(7)
    print(calculator2.calculate_area())