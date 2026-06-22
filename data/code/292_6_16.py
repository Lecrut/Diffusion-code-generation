def calculate_perimeter(side_lengths):
    perimeter = 0
    for length in side_lengths:
        perimeter += length
    return perimeter

if __name__ == '__main__':
    sample_sides = [7, 5, 3, 8, 2]
    total_perimeter = calculate_perimeter(sample_sides)
    print(total_perimeter)