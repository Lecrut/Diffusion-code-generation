def _validate_positive(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def get_triangle_area(base, height):
    _validate_positive(base, "base")
    _validate_positive(height, "height")
    return base * height * 0.5

if __name__ == '__main__':
    b = 12
    h = 4
    print(get_triangle_area(b, h))