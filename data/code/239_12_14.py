def calculate_perimeter(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        sample_length = 7.5
        sample_width = 3.2
        perimeter = calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)