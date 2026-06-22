def _validate_dimensions(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric.")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return True

def triangle_area(base, height):
    _validate_dimensions(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    b = 8.0
    h = 12.0
    result = triangle_area(b, h)
    print(result)