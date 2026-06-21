def get_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    side1, side2, side3 = sides
    return side1 + side2 + side3

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    perimeter = get_perimeter(sample_sides)
    print(perimeter)