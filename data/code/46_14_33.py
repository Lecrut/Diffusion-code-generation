def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return sum([side1, side2, side3])

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)