def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_length = 8
    sample_width = 4
    result = calculate_rectangle_perimeter(sample_length, sample_width)
    print(result)