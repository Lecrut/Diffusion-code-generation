def calculate_rectangle_perimeter(length, width):
    if not (isinstance(length, int) and isinstance(width, int)) or length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 11
    sample_width = 7
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)