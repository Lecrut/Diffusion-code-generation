def validate_sides(sides):
    if not isinstance(sides, list):
        raise ValueError("Input must be a list.")
    if len(sides) == 0:
        return 0
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All sides must be positive numbers.")

def calculate_perimeter_of_polygon(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    polygon_sides = [3, 4, 5, 6]
    perimeter = calculate_perimeter_of_polygon(polygon_sides)
    print(perimeter)