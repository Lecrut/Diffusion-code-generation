def validate_sides(sides):
    if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers")

def calculate_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [5, 3, 4, 2]
    print(calculate_perimeter(sample_sides))