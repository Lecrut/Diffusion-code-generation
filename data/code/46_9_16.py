def validate_sides(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return True

def calculate_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [7, 24, 25]
    perimeter = calculate_perimeter(triangle_sides)
    print(perimeter)