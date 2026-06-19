def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        sample_length = 9
        sample_width = 5
        perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)