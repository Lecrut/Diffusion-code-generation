class SquareCalculator:
    SIDE_LENGTH = 3

    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    calculator = SquareCalculator()
    area = calculator.calculate_area(SquareCalculator.SIDE_LENGTH)
    print(area)