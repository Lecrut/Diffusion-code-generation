def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side_a = 6
    side_b = 8
    side_c = 10
    perimeter_result = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(perimeter_result)