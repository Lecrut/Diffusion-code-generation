def _validate_dimension(value, name):
    if value < 0:
        raise ValueError(f"{name} cannot be negative")

def rectangle_area(width, height):
    _validate_dimension(width, "width")
    _validate_dimension(height, "height")
    return width * height

if __name__ == '__main__':
    try:
        area = rectangle_area(12, 7)
        print(area)
    except ValueError as err:
        print(err)