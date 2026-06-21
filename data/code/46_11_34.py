def calculate_triangle_perimeter(side1, side2, side3):
    MIN_SIDE_LENGTH = 0.0001
    if not all((isinstance(side, (int, float)) and side > MIN_SIDE_LENGTH for side in [side1, side2, side3])):
        raise ValueError('Side lengths must be positive numbers greater than 0.0001.')
    return side1 + side2 + side3
if __name__ == '__main__':
    try:
        side_a = 3.5
        side_b = 4.2
        side_c = 5.8
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)