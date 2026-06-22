import argparse

class SquareAreaCalculator:

    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

def main():
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    try:
        calculator = SquareAreaCalculator(args.side_length)
        print(calculator.calculate_area())
        sample_side_length = 5.0
        sample_calculator = SquareAreaCalculator(sample_side_length)
        print(sample_calculator.calculate_area())
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()