def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)