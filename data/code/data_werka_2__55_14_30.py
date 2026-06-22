def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(s, (int, float)) for s in (side1, side2, side3)):
        raise ValueError("All sides must be numbers")
    if any(s <= 0 for s in (side1, side2, side3)):
        raise ValueError("All sides must be positive numbers")
    return sum((side1, side2, side3))

if __name__ == '__main__':
    SAMPLE_SIDE_1 = 7
    SAMPLE_SIDE_2 = 10
    SAMPLE_SIDE_3 = 5
    perimeter = calculate_triangle_perimeter(SAMPLE_SIDE_1, SAMPLE_SIDE_2, SAMPLE_SIDE_3)
    print(perimeter)