import argparse

def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if not (a + b > c and a + c > b and (b + c > a)):
        return False
    return True

def calculate_perimeter(a, b, c):
    if is_valid_triangle(a, b, c):
        return a + b + c
    else:
        raise ValueError('The given side lengths do not form a valid triangle.')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle.')
    parser.add_argument('side1', type=float, help='Length of the first side')
    parser.add_argument('side2', type=float, help='Length of the second side')
    parser.add_argument('side3', type=float, help='Length of the third side')
    args = parser.parse_args()
    try:
        perimeter = calculate_perimeter(args.side1, args.side2, args.side3)
        print(f'The perimeter of the triangle is: {perimeter}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f'Perimeter of (3, 4, 5): {result1}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        result2 = calculate_perimeter(1, 2, 10)
        print(f'Perimeter of (1, 2, 10): {result2}')
    except ValueError as e:
        print(f'Error: {e}')