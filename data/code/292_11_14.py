def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle side lengths.")
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f"Perimeter for sides (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = calculate_perimeter(-1, 4, 5)
        print(f"Perimeter for sides (-1, 4, 5): {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = calculate_perimeter(3, 7, 1)
        print(f"Perimeter for sides (3, 7, 1): {result3}")
    except ValueError as e:
        print(f"Error: {e}")