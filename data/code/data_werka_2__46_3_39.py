def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("All sides must be positive integers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(7, 9, 12)
        print(perimeter)
    except ValueError as e:
        print(e)