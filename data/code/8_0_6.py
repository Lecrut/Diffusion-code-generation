def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    return length * width

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    result = calculate_rectangle_area(sample_length, sample_width)
    print(result)