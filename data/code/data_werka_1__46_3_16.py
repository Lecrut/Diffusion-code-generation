import argparse

def validate_side_length(side):
    if side <= 0:
        raise ValueError(f'Side length {side} must be positive.')
    return side

def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and (b + c > a):
        return True
    else:
        raise ValueError('The given side lengths do not form a valid triangle.')

def calculate_triangle_perimeter(a, b, c):
    try:
        a = validate_side_length(a)
        b = validate_side_length(b)
        c = validate_side_length(c)
        if is_valid_triangle(a, b, c):
            return a + b + c
    except ValueError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle.')
    parser.add_argument('side1', type=float, help='Length of the first side')
    parser.add_argument('side2', type=float, help='Length of the second side')
    parser.add_argument('side3', type=float, help='Length of the third side')
    args = parser.parse_args()
    perimeter = calculate_triangle_perimeter(args.side1, args.side2, args.side3)
    if perimeter is not None:
        print(f'The perimeter of the triangle is: {perimeter}')
    sample_values = [(3, 4, 5), (6, 8, 10), (7, 24, 25), (1, 2, 3)]
    for sides in sample_values:
        perimeter = calculate_triangle_perimeter(*sides)
        if perimeter is not None:
            print(f'The perimeter of the triangle with sides {sides} is: {perimeter}')