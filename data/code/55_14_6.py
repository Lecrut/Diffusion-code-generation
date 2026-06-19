def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All sides must be numeric types.")
    if any(x <= 0 for x in [a, b, c]):
        raise ValueError("Side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
        print(calculate_triangle_perimeter(7.5, 9.2, 4.8))
        print(calculate_triangle_perimeter(10, 10, 10))
    except ValueError as e:
        print(e)