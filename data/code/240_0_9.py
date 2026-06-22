class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 5
    calculator = SquareCalculator(sample_side_length)
    area = calculator.calculate_area(calculator.side_length)
    print(f"The side length entered is: {sample_side_length}")
    print(f"The area of the square is: {area}")