def validate_sides(sides):
    if not sides:
        raise ValueError("Sides list cannot be empty")
    for side in sides:
        if side <= 0:
            raise ValueError("Side length must be greater than zero")

def calculate_polygon_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    perimeter = calculate_polygon_perimeter(sample_sides)
    print(perimeter)