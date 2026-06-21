def validate_dimensions(length, width):
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")

def calculate_rectangle_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    sample_length = 6.0
    sample_width = 4.0
    area_result = calculate_rectangle_area(sample_length, sample_width)
    print(area_result)