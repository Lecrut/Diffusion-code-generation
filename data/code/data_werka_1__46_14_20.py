def calculate_triangle_perimeter(a, b, c):
    if any((x <= 0 for x in (a, b, c))):
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(5, 12, 13))
        print(calculate_triangle_perimeter(7, 24, 25))
        print(calculate_triangle_perimeter(1, 1, 2))
    except ValueError as e:
        print(e)