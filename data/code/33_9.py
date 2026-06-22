def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric types")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = compute_triangle_area(sample_base, sample_height)
    print(result)
    sample_base_invalid = "10"
    sample_height_valid = 5
    try:
        invalid_result = compute_triangle_area(sample_base_invalid, sample_height_valid)
    except TypeError as e:
        print(str(e))
    sample_negative_base = -5
    sample_positive_height = 10
    try:
        negative_result = compute_triangle_area(sample_negative_base, sample_positive_height)
    except ValueError as e:
        print(str(e))