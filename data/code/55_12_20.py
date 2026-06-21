def get_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Input must be a tuple of three numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (3, 4, 5)
    print(get_perimeter(sample_sides))