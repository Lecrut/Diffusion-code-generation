def calculate_triangle_perimeter(a, b, c):
    if not all((isinstance(x, (int, float)) for x in [a, b, c])):
        raise TypeError('All side lengths must be numbers.')
    if any((x <= 0 for x in [a, b, c])):
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    return a + b + c
if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(1, 1, 2))
    except (ValueError, TypeError) as e:
        print(e)