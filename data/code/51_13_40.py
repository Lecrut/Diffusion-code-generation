def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 2
    try:
        perimeter = calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)