def calculate_perimeter(sides):
    numeric_types = {int, float}
    if not all(isinstance(side, numeric_types) for side in sides):
        raise ValueError("All sides must be numeric")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)