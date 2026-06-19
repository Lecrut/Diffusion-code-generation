def calculate_perimeter(sides):
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 24, 25]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)