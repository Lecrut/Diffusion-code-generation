import argparse

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c

def main():
    parser = argparse.ArgumentParser(description='Calculate the perimeter of a triangle given its side lengths.')
    parser.add_argument('a', type=float, help='Length of the first side')
    parser.add_argument('b', type=float, help='Length of the second side')
    parser.add_argument('c', type=float, help='Length of the third side')
    args = parser.parse_args()
    try:
        perimeter = calculate_triangle_perimeter(args.a, args.b, args.c)
        print(f'The perimeter of the triangle is: {perimeter}')
    except ValueError as e:
        print(f'Error: {e}')
if __name__ == '__main__':
    sample_values = [(3, 4, 5), (1, 2, 3), (7, 8, 9)]
    for sides in sample_values:
        try:
            perimeter = calculate_triangle_perimeter(*sides)
            print(f'Perimeter of {sides}: {perimeter}')
        except ValueError as e:
            print(f'Error with sides {sides}: {e}')