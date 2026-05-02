def calculate_triangle_perimeter(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        raise ValueError("All sides must be positive numbers")
if __name__ == '__main__':
    side_a = 3
    side_b = 4
    side_c = 5
    try:
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    side_x = -1
    side_y = 5
    side_z = 10
    try:
        perimeter = calculate_triangle_perimeter(side_x, side_y, side_z)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")