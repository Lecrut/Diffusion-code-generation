def calculate_triangle_perimeter(a, b, c):
    if not all((isinstance(x, (int, float)) for x in [a, b, c])):
        raise TypeError('All sides must be numbers.')
    if any((x <= 0 for x in [a, b, c])):
        raise ValueError('All sides must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7, 8, 9))
        print(calculate_triangle_perimeter(10, 10, 10))
        print(calculate_triangle_perimeter(0.5, 0.5, 0.7))
        print(calculate_triangle_perimeter(1, 2, 3))
    except (TypeError, ValueError) as e:
        print(e)