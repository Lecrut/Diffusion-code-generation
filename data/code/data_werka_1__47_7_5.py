def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    length = 9
    width = 6
    area = calculate_area(length, width)
    print(area)