def _validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def compute_triangle_area(base, height):
    _validate_positive(base, "base")
    _validate_positive(height, "height")
    return base * height * 0.5

if __name__ == '__main__':
    base_value = 12
    height_value = 8
    result = compute_triangle_area(base_value, height_value)
    print(result)