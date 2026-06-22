def _validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be a positive number, got {value}")
    return float(value)

def compute_triangle_area(base, height):
    valid_base = _validate_positive(base, "base")
    valid_height = _validate_positive(height, "height")
    return 0.5 * valid_base * valid_height

if __name__ == '__main__':
    base_val = 12.5
    height_val = 8.0
    result = compute_triangle_area(base_val, height_val)
    print(result)