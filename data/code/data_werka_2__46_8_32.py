def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if not all(isinstance(x, (int, float)) and x > 0 for x in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_side_a = 7
    sample_side_b = 8
    sample_side_c = 9
    perimeter_result = calculate_triangle_perimeter(sample_side_a, sample_side_b, sample_side_c)
    print(perimeter_result)