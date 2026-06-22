def calculate_rectangle_perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 15
    sample_width = 8
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)