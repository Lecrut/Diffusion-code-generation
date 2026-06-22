import argparse
MIN_SIDE_LENGTH = 0.0

def calculate_square_area(side_length):
    if side_length <= MIN_SIDE_LENGTH:
        raise ValueError('Side length must be positive')
    return side_length * side_length
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    try:
        area = calculate_square_area(args.side_length)
        print(area)
    except ValueError as e:
        print(e)
    sample_side_length = 5.0
    try:
        sample_area = calculate_square_area(sample_side_length)
        print(sample_area)
    except ValueError as e:
        print(e)