def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Both length and width must be numbers")

def calculate_rectangle_area(length, width):
    validate_dimensions(length, width)
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_rectangle_area(5, 3)
        print(area)
    except ValueError as e:
        print(e)