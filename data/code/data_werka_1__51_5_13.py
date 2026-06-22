def calculate_polygon_perimeter(sides):
    if not isinstance(sides, list):
        raise TypeError("Input must be a list of side lengths.")
    if len(sides) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    try:
        polygon_sides = [3, 4, 5]
        perimeter = calculate_polygon_perimeter(polygon_sides)
        print(perimeter)
    except Exception as e:
        print(f"Error: {e}")