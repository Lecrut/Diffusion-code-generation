def calculate_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        sample_length = 6
        sample_width = 2
        perimeter = calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)