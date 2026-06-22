def validate_dimensions(length, width):
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")

def calculate_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    LENGTH = 30
    WIDTH = 15
    try:
        area = calculate_area(LENGTH, WIDTH)
        print(area)
    except ValueError as e:
        print(e)