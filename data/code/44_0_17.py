def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)

if __name__ == '__main__':
    SAMPLE_LENGTH = 9
    SAMPLE_WIDTH = 5
    perimeter = calculate_rectangle_perimeter(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(perimeter)