def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    return a + b + c
if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    side4 = 1
    side5 = -2
    side6 = 5
    try:
        perimeter = calculate_triangle_perimeter(side4, side5, side6)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")