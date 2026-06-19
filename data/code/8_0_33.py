def calculate_rectangle_area(length, width):
    if length <= 0:
        raise ValueError("Length must be positive")
    if width <= 0:
        raise ValueError("Width must be positive")
    return length * width

if __name__ == '__main__':
    try:
        sample_length = 5.0
        sample_width = 3.0
        area = calculate_rectangle_area(sample_length, sample_width)
        print(area)
    except ValueError as e:
        print(e)