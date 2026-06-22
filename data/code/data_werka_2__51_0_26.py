def calculate_perimeter(sides):
    if not sides:
        return 0
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)