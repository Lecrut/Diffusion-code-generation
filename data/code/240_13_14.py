class SquareAreaCalculator:
    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    print(calculator.calculate_area(5))