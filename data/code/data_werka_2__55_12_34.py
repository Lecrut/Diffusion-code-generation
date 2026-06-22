def get_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    side1, side2, side3 = sides
    perimeter = side1 + side2 + side3
    return perimeter

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    print(get_perimeter(sample_sides))