def calculate_triangle_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 9, 12]
    perimeter = calculate_triangle_perimeter(sample_sides)
    print(perimeter)