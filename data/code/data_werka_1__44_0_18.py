def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_length = 9
    sample_width = 5
    try:
        calculated_perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
        print(calculated_perimeter)
    except ValueError as e:
        print(e)