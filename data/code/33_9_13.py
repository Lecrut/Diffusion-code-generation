def compute_triangle_area(base, height):
    try:
        base_val = float(base)
        height_val = float(height)
    except (TypeError, ValueError):
        raise ValueError("Base and height must be numeric values")
    if base_val < 0 or height_val < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base_val * height_val

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)
    result2 = compute_triangle_area(7.5, 3)
    print(result2)
    try:
        compute_triangle_area("invalid", 5)
    except ValueError as e:
        print(e)