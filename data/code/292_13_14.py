def calculate_polygon_perimeter(sides):
    if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    perimeter = calculate_polygon_perimeter(sample_sides)
    print(perimeter)