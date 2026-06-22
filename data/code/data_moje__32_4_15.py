def _validate_dimensions(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("width must be numeric")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric")
    if width < 0:
        raise ValueError("width must be non-negative")
    if height < 0:
        raise ValueError("height must be non-negative")

def get_rectangle_area(width, height):
    _validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    w = 7
    h = 3
    print(get_rectangle_area(w, h))