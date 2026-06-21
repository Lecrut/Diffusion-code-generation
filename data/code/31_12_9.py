class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    side_length = 7
    calculator = SquareCalculator(side_length)
    area = calculator.get_area()
    print(area)
    perimeter = calculator.get_perimeter()
    print(perimeter)