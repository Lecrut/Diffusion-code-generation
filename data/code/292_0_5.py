def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_length = 15
    sample_width = 7
    perimeter_result = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter_result)