def get_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    result = get_perimeter(sample_sides)
    print(result)