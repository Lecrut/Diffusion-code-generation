def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    try:
        sample_length = 10
        sample_width = 6
        result_perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
        print(result_perimeter)
    except ValueError as e:
        print(e)