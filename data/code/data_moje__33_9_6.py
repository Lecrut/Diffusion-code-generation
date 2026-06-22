def compute_triangle_area(base, height):
    try:
        base_val = float(base)
        height_val = float(height)
    except (ValueError, TypeError):
        raise ValueError("Base and height must be numeric values.")
    if base_val < 0 or height_val < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base_val * height_val

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = compute_triangle_area(sample_base, sample_height)
    print(area)
    invalid_base = "invalid"
    try:
        compute_triangle_area(invalid_base, sample_height)
    except ValueError as e:
        print(str(e))
    negative_base = -5
    try:
        compute_triangle_area(negative_base, sample_height)
    except ValueError as e:
        print(str(e))