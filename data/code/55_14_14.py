def calculate_triangle_perimeter(a, b, c):
    if not all((isinstance(x, (int, float)) for x in [a, b, c])):
        raise ValueError('All sides must be numeric types.')
    if any((x <= 0 for x in [a, b, c])):
        raise ValueError('Side lengths must be positive numbers.')
    return a + b + c
if __name__ == '__main__':
    try:
        perimeter1 = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter1)
        perimeter2 = calculate_triangle_perimeter(6.0, 8.0, 10.0)
        print(perimeter2)
        perimeter3 = calculate_triangle_perimeter(-3, 4, 5)
    except ValueError as e:
        print(e)