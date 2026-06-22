TRIANGLE_SIDES_COUNT = 3

def get_perimeter(sides):
    if len(sides) != TRIANGLE_SIDES_COUNT:
        raise ValueError("Input must be a tuple of three numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    print(get_perimeter(sample_sides))