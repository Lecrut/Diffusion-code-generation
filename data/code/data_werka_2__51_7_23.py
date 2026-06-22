def calculate_perimeter(sides):
    total = 0
    for side in sides:
        if not isinstance(side, (int, float)):
            raise ValueError("All sides must be numeric values.")
        total += side
    return total

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)