def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in (side1, side2, side3)):
        raise ValueError("Side lengths must be positive numbers.")
    return sum((side1, side2, side3))

if __name__ == '__main__':
    try:
        triangle_sides = {
            'side1': 7,
            'side2': 9,
            'side3': 12
        }
        perimeter = calculate_triangle_perimeter(triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3'])
        print(perimeter)
    except ValueError as e:
        print(e)