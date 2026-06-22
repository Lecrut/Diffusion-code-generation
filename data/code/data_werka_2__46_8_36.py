def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")
    return sum([side1, side2, side3])

if __name__ == '__main__':
    sample_sides = {
        'side1': 7.5,
        'side2': 9.0,
        'side3': 6.5
    }
    perimeter = calculate_triangle_perimeter(**sample_sides)
    print(perimeter)