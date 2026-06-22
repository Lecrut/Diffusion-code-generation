def is_positive_number(value):
    return value > 0

def calculate_area(length, width):
    if not is_positive_number(length) or not is_positive_number(width):
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == '__main__':
    SAMPLE_LENGTH = 8.5
    SAMPLE_WIDTH = 1.2
    area_result = calculate_area(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(area_result)