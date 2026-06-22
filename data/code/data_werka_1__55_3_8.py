def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Triangle sides must be positive numbers.")
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise ValueError("The given sides do not form a valid triangle.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 7.0
        side_b = 10.0
        side_c = 5.0
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)