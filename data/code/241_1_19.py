def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def calculate_rectangle_area(length, width):
    validate_numeric(length)
    validate_numeric(width)
    return length * width

if __name__ == '__main__':
    try:
        area = calculate_rectangle_area(5, 3)
        print(area)
    except ValueError as e:
        print(e)