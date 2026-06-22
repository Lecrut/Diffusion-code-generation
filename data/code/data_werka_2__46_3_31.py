def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(x, int) and x > 0 for x in (side1, side2, side3)):
        raise ValueError("All sides must be positive integers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 9
        side_c = 12
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)