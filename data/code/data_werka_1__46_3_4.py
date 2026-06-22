import argparse

def calculate_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle.')
    parser.add_argument('side1', type=float, help='Length of the first side')
    parser.add_argument('side2', type=float, help='Length of the second side')
    parser.add_argument('side3', type=float, help='Length of the third side')
    args = parser.parse_args()
    perimeter = calculate_perimeter(args.side1, args.side2, args.side3)
    print(perimeter)
    sample_perimeter = calculate_perimeter(3.0, 4.0, 5.0)
    print(sample_perimeter)