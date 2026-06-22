def calculate_triangle_perimeter(a, b, c):
    POSITIVE_THRESHOLD = 0
    if not all(isinstance(x, (int, float)) and x > POSITIVE_THRESHOLD for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5, 12, 13)
        print(perimeter)
    except ValueError as e:
        print(e)