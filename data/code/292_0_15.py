def calculate_rectangle_perimeter(length, width):
    PERIMETER_CONSTANT = 2
    return PERIMETER_CONSTANT * (length + width)

if __name__ == '__main__':
    SAMPLE_LENGTH = 10
    SAMPLE_WIDTH = 5
    perimeter_result = calculate_rectangle_perimeter(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(perimeter_result)