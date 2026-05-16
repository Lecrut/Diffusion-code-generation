def calculate_triangle_perimeter(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        raise ValueError("All side lengths must be positive numbers.")
if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    side4 = -1
    side5 = 5
    side6 = 10
    try:
        perimeter = calculate_triangle_perimeter(side4, side5, side6)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")