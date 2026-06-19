def calculate_triangle_perimeter(a, b, c):
    MIN_SIDE_LENGTH = 0.0001
    if not all((isinstance(x, (int, float)) and x > MIN_SIDE_LENGTH for x in [a, b, c])):
        raise ValueError('Side lengths must be positive numbers greater than the minimum threshold.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(10, 6, 8))
        print(calculate_triangle_perimeter(2, 2, 4))
    except ValueError as e:
        print(e)