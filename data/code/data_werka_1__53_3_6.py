import argparse

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    
    square_instance = Square(args.side_length)
    area_from_cli = square_instance.calculate_area(square_instance.side_length)
    print(area_from_cli)

    sample_side_length = 5.0
    sample_square = Square(sample_side_length)
    sample_area = sample_square.calculate_area(sample_square.side_length)
    print(sample_area)