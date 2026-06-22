class SquareAreaCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 5
    calculator = SquareAreaCalculator(sample_side_length)
    area = calculator.calculate_area(sample_side_length)
    print(f"The area of the square with side length {sample_side_length} is: {area}")