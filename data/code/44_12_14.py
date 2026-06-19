def calculate_rectangle_perimeter(length, width):
    total_length = 2 * length
    total_width = 2 * width
    return total_length + total_width

if __name__ == '__main__':
    sample_length = 12
    sample_width = 6
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)