import argparse

def calculate_square_area(side_length):
    return side_length * side_length
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    args = parser.parse_args()
    sample_values = {'sample_side_length': 5.0, 'another_sample_side_length': 10.0}
    for key, value in sample_values.items():
        area = calculate_square_area(value)
        print(f'Area of square with side length {value}: {area}')