def calculate_triangle_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required.")
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_triangle_sides = [5, 12, 13]
    try:
        perimeter = calculate_triangle_perimeter(sample_triangle_sides)
        print(perimeter)
    except ValueError as e:
        print(e)