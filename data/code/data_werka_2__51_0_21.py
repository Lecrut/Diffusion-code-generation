def calculate_perimeter(sides):
    perimeter = 0
    for side in sides:
        perimeter += side
    return perimeter

if __name__ == '__main__':
    sample_sides = [7, 8, 9]
    result = calculate_perimeter(sample_sides)
    print(result)