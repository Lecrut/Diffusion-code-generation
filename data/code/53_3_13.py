import argparse

def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Invalid input: Side length must be positive')
    return side_length * side_length

class SquareAreaCalculator:

    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return calculate_square_area(self.side_length)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    try:
        calculator = SquareAreaCalculator(args.side_length)
        print(calculator.get_area())
    except ValueError as e:
        print(e)
    sample_side_length = 5.0
    try:
        sample_calculator = SquareAreaCalculator(sample_side_length)
        print(sample_calculator.get_area())
    except ValueError as e:
        print(e)