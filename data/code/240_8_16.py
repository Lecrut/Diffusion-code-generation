class SquareAreaCalculator:
    def calculate_area(self, side):
        return side * side

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    print(calculator.calculate_area(5))
    print(calculator.calculate_area(0))
    print(calculator.calculate_area(100))