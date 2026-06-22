def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    SAMPLE_LENGTH = 6.2
    SAMPLE_WIDTH = 4.8
    area_result = calculate_area(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(area_result)