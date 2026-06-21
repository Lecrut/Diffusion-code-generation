def get_perimeter(sides):
    if not isinstance(sides, tuple) or len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (7, 24, 25)
    print(get_perimeter(sample_sides))