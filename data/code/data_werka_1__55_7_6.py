def calculate_triangle_perimeter(a, b, c):
    MIN_SIDE_LENGTH = 0.0
    if not all(isinstance(x, (int, float)) and x > MIN_SIDE_LENGTH for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(10, 15, 20)
        print(perimeter)
    except ValueError as e:
        print(e)