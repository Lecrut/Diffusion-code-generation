def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f"Perimeter for sides 3, 4, 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = calculate_perimeter(7, 8, 9)
        print(f"Perimeter for sides 7, 8, 9: {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = calculate_perimeter(-1, 4, 5)
        print(f"Perimeter for sides -1, 4, 5: {result3}")
    except ValueError as e:
        print(f"Error: {e}")