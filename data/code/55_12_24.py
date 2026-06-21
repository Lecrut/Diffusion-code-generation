def get_perimeter(sides):
    if len(sides) != 3 or any(side <= 0 for side in sides):
        raise ValueError("Input must be a tuple of three positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = (3, 4, 5)
    print(get_perimeter(sample_sides))