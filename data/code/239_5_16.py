def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 6
    sample_width = 4
    perimeter_value = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter_value)