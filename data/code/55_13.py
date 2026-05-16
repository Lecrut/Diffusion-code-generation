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
    try:
        calculate_triangle_perimeter(3, -4, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        calculate_triangle_perimeter(1, 2, 0)
    except ValueError as e:
        print(f"Error: {e}")