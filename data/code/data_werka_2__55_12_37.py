def validate_triangle_sides(sides):
    if not isinstance(sides, tuple) or len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All sides must be positive numbers.")

def get_perimeter(sides):
    validate_triangle_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (9, 12, 15)
    print(get_perimeter(sample_sides))