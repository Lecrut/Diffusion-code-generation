def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    a = 6
    b = 8
    c = 10
    triangle_perimeter = calculate_triangle_perimeter(a, b, c)
    print(triangle_perimeter)