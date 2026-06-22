def validate_sides(sides):
    if not isinstance(sides, tuple) or len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    for side in sides:
        if not isinstance(side, (int, float)):
            raise ValueError("All elements must be numbers.")

def get_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    print(get_perimeter(sample_sides))