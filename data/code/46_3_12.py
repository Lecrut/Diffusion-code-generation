import argparse

def validate_triangle_sides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lengths do not form a valid triangle.")

def calculate_triangle_perimeter(a, b, c):
    validate_triangle_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = calculate_triangle_perimeter(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = calculate_triangle_perimeter(7, 10, 5)
        print(f"Perimeter of (7, 10, 5): {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = calculate_triangle_perimeter(1, 2, 3)
        print(f"Perimeter of (1, 2, 3): {result3}")
    except ValueError as e:
        print(f"Error: {e}")