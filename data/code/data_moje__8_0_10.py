def calculate_rectangle_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric values.")
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 10.0
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)