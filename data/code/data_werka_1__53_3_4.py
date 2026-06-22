import argparse

def calculate_square_area(side_length):
    return side_length * side_length

class SquareAreaCalculator:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def get_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    
    calculated_area = calculate_square_area(args.side_length)
    print(calculated_area)
    
    sample_side_length = 3.0
    calculator = SquareAreaCalculator(sample_side_length)
    sample_area = calculator.get_area()
    print(sample_area)