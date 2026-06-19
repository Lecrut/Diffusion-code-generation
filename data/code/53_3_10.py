import argparse

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    
    square_instance = Square(args.side_length)
    print(square_instance.calculate_area())
    
    sample_side_length = 5.0
    sample_square = Square(sample_side_length)
    print(sample_square.calculate_area())