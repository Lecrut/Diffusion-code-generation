def validate_sides(sides):
    if not all(side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")

def calculate_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_triangle = [7, 10, 5]
    perimeter = calculate_perimeter(sample_triangle)
    print(perimeter)