import argparse

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c

def main():
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle.')
    parser.add_argument('side1', type=float, help='Length of the first side')
    parser.add_argument('side2', type=float, help='Length of the second side')
    parser.add_argument('side3', type=float, help='Length of the third side')
    args = parser.parse_args()
    try:
        perimeter = calculate_triangle_perimeter(args.side1, args.side2, args.side3)
        print(f'The perimeter of the triangle is: {perimeter}')
    except ValueError as e:
        print(f'Error: {e}')
if __name__ == '__main__':
    try:
        sample_perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(f'Sample perimeter of (6, 8, 10): {sample_perimeter}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        sample_perimeter2 = calculate_triangle_perimeter(7, 10, 5)
        print(f'Sample perimeter of (7, 10, 5): {sample_perimeter2}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        invalid_perimeter = calculate_triangle_perimeter(1, 1, 3)
        print(f'Invalid perimeter of (1, 1, 3): {invalid_perimeter}')
    except ValueError as e:
        print(f'Error: {e}')