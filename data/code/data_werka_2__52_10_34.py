RECTANGLE_LENGTH = 25
RECTANGLE_WIDTH = 10

def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_rectangle_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    area = calculate_rectangle_area(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    print(area)