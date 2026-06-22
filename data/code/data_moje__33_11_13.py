def _validate_dimensions(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base, height

def compute_triangle_area(base, height):
    valid_base, valid_height = _validate_dimensions(base, height)
    return 0.5 * valid_base * valid_height

if __name__ == '__main__':
    base_value = 8
    height_value = 6
    print(compute_triangle_area(base_value, height_value))