import argparse

def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the area of a square.')
    parser.add_argument('side_length', type=float, help='The length of a side of the square')
    
    args = parser.parse_args()
    
    area = calculate_square_area(args.side_length)
    print(area)