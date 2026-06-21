def calculate_perimeter(sides):
    MIN_SIDE_LENGTH = 0
    if any(side <= MIN_SIDE_LENGTH for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_triangle_sides = [5, 12, 13]
    perimeter_result = calculate_perimeter(sample_triangle_sides)
    print(perimeter_result)