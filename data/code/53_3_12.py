import argparse

def calculate_square_area(side_length):
    return side_length * side_length
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    units = {'cm': 'square centimeters', 'm': 'square meters'}
    area = calculate_square_area(args.side_length)
    print(f"The area of the square is {area} {units['cm']}")
    sample_side_length = 5.0
    sample_area = calculate_square_area(sample_side_length)
    print(f"Sample area: {sample_area} {units['m']}")