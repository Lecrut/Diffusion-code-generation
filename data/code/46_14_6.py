def calculate_triangle_perimeter(a, b, c):
    MIN_SIDE_LENGTH = 0.0001
    if a <= MIN_SIDE_LENGTH or b <= MIN_SIDE_LENGTH or c <= MIN_SIDE_LENGTH:
        raise ValueError('Side lengths must be greater than zero.')
    if not (a + b > c and a + c > b and (b + c > a)):
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(2.5, 3.5, 4.5))
        print(calculate_triangle_perimeter(1, 1, 2))
    except ValueError as e:
        print(e)