class SquareAreaCalculator:
    def calculate_area(self, side):
        return side * side

if __name__ == '__main__':
    calculator = SquareAreaCalculator()
    area = calculator.calculate_area(5)
    print(area)