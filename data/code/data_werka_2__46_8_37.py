def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    sample_side1 = 7.5
    sample_side2 = 9.2
    sample_side3 = 4.8
    try:
        perimeter = calculate_triangle_perimeter(sample_side1, sample_side2, sample_side3)
        print(perimeter)
    except ValueError as e:
        print(e)