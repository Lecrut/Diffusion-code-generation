def calculate_triangle_perimeter(side1, side2, side3):
    if not all((isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3])):
        raise ValueError('Side lengths must be positive numbers.')
    return side1 + side2 + side3
if __name__ == '__main__':
    try:
        sides = [7.5, 9.2, 4.8]
        perimeter = calculate_triangle_perimeter(*sides)
        print(perimeter)
    except ValueError as e:
        print(e)