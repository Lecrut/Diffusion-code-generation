def calculate_perimeter(length, width):
    sum_of_sides = length + width
    perimeter = 2 * sum_of_sides
    return perimeter

if __name__ == '__main__':
    sample_length = 8
    sample_width = 6
    calculated_perimeter = calculate_perimeter(sample_length, sample_width)
    print(calculated_perimeter)