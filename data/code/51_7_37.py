def calculate_perimeter(sides):
    try:
        return sum(float(side) for side in sides)
    except (ValueError, TypeError):
        raise ValueError("All sides must be numeric")

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)