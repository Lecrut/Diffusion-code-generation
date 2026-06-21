def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return sum([side1, side2, side3])

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)