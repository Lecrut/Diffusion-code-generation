def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        a = 6
        b = 8
        c = 10
        perimeter = calculate_triangle_perimeter(a, b, c)
        print(perimeter)
    except ValueError as e:
        print(e)