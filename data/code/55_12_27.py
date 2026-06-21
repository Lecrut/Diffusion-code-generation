def get_perimeter(sides):
    if not isinstance(sides, tuple) or len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    if any(not isinstance(side, (int, float)) for side in sides):
        raise ValueError("All elements in the tuple must be numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    print(get_perimeter(sample_sides))