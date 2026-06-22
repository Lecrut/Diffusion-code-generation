def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_lengths = [7.5, 9.2, 4.8]
        perimeter = calculate_triangle_perimeter(*side_lengths)
        print(perimeter)
    except ValueError as e:
        print(e)