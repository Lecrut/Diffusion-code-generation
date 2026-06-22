def _validate_dimensions(w, h):
    if w <= 0 or h <= 0:
        raise ValueError("Dimensions must be positive")
    return True

def calculate_area(width, height):
    _validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    w = 8
    h = 12
    print(calculate_area(w, h))