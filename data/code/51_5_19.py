def validate_sides(sides):
    if not isinstance(sides, list):
        raise ValueError("Input must be a list of side lengths.")
    if len(sides) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All sides must be positive numbers.")

def calculate_polygon_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    polygon_sides = [3, 4, 5]
    perimeter = calculate_polygon_perimeter(polygon_sides)
    print(perimeter)