def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

def calculate_area(length, width):
    return length * width

if __name__ == '__main__':
    try:
        validate_dimensions(10, 5)
        area_result = calculate_area(10, 5)
        print(area_result)
    except ValueError as e:
        print(e)