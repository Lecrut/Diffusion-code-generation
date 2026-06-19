def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 9
    sample_width = 5
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)