def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers")
    return a + b + c
if __name__ == '__main__':
    side_a = 3
    side_b = 4
    side_c = 5
    try:
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    side_a_invalid = -1
    side_b_invalid = 4
    side_c_invalid = 5
    try:
        perimeter_invalid = calculate_triangle_perimeter(side_a_invalid, side_b_invalid, side_c_invalid)
        print(perimeter_invalid)
    except ValueError as e:
        print(f"Error: {e}")