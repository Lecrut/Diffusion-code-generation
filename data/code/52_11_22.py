def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 2.4
    area_result = calculate_rectangle_area(sample_length, sample_width)
    print(area_result)