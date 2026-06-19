import argparse

def calculate_square_area(side_length):
    if side_length <= 0:
        return None
    return side_length * side_length
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    area = calculate_square_area(args.side_length)
    if area is not None:
        print(area)
    else:
        print('Invalid input: Side length must be positive')
    sample_side_length = 5.0
    sample_area = calculate_square_area(sample_side_length)
    if sample_area is not None:
        print(sample_area)