def calculate_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_perimeter(1, 2, 10)
        print(f"Perimeter of (1, 2, 10): {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = calculate_perimeter(5, 5, 5)
        print(f"Perimeter of (5, 5, 5): {result3}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result4 = calculate_perimeter(10, 2, 3)
        print(f"Perimeter of (10, 2, 3): {result4}")
    except ValueError as e:
        print(f"Error: {e}")