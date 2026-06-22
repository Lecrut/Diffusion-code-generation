def _validate_dimension(value, dimension_name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{dimension_name} must be a number")
    if value <= 0:
        raise ValueError(f"{dimension_name} must be greater than zero")

def calculate_rectangle_area(width, height):
    _validate_dimension(width, "Width")
    _validate_dimension(height, "Height")
    return width * height

if __name__ == '__main__':
    test_width = 7.25
    test_height = 4.1
    try:
        computed_area = calculate_rectangle_area(test_width, test_height)
        print(computed_area)
    except (TypeError, ValueError) as error:
        print(error)