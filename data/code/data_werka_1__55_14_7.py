def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise ValueError("All sides must be numeric types.")
    if any(side <= 0 for side in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)