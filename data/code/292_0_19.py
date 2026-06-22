def calculate_rectangle_perimeter(length, width):
    PERIMETER_FACTOR = 2
    return PERIMETER_FACTOR * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 5
    perimeter_result = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter_result)