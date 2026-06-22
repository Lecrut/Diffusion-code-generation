class SquareAreaCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    calculator = SquareAreaCalculator(5.0)
    area = calculator.calculate_area(calculator.side_length)
    print(f"The side length of the square is: {calculator.side_length}")
    print(f"The area of the square is: {area}")