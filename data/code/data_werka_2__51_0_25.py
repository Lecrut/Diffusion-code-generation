def calculate_perimeter(sides):
    total = 0
    for side in sides:
        total += side
    return total

if __name__ == '__main__':
    sample_sides = [7, 8, 9]
    perimeter_result = calculate_perimeter(sample_sides)
    print(perimeter_result)