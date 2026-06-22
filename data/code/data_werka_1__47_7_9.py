def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    try:
        length = 12
        width = 4
        area = calculate_area(length, width)
        print(area)
    except ValueError as e:
        print(e)