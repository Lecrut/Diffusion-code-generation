def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    sample_sides = [(2, 3, 4), (5, 12, 13), (7, 24, 25)]
    for sides in sample_sides:
        perimeter = calculate_triangle_perimeter(*sides)
        print(perimeter)