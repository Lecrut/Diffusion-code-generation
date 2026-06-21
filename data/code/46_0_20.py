def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise ValueError("The side lengths do not form a valid triangle.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side1 = 5
        side2 = 6
        side3 = 7
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)