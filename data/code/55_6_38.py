def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("All sides must be numbers")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(10, 15, 20)
        print(perimeter)
    except (ValueError, TypeError) as e:
        print(e)