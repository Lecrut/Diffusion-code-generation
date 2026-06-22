def calculate_perimeter(length, width):
    MIN_DIMENSION = 0
    if length <= MIN_DIMENSION or width <= MIN_DIMENSION:
        raise ValueError("Length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    SAMPLE_LENGTH = 10
    SAMPLE_WIDTH = 6
    try:
        perimeter = calculate_perimeter(SAMPLE_LENGTH, SAMPLE_WIDTH)
        print(perimeter)
    except ValueError as e:
        print(e)