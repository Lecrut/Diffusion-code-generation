def triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    try:
        result1 = triangle_perimeter(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = triangle_perimeter(1, 2, 10)
        print(f"Perimeter of (1, 2, 10): {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = triangle_perimeter(-1, 2, 3)
        print(f"Perimeter of (-1, 2, 3): {result3}")
    except ValueError as e:
        print(f"Error: {e}")