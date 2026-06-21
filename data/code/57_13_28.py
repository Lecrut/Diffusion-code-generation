def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == '__main__':
    sample_length = 8.2
    sample_width = 4.5
    area_result = calculate_area(sample_length, sample_width)
    print(area_result)