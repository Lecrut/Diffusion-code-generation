def calculate_triangle_perimeter(side1, side2, side3):
    if any(side <= 0 for side in (side1, side2, side3)):
        raise ValueError('Side lengths must be positive numbers.')
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 8
        side_c = 9
        perimeter_result = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter_result)
    except ValueError as e:
        print(e)