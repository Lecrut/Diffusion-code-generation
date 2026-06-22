def validate_sides(sides):
    if not sides or any(side <= 0 for side in sides):
        raise ValueError("Sides must be a list of positive numbers")

def calculate_polygon_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    perimeter = calculate_polygon_perimeter(sample_sides)
    print(perimeter)