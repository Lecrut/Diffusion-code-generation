def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("base must be a numeric type")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a numeric type")
    if base < 0:
        raise ValueError("base must be non-negative")
    if height < 0:
        raise ValueError("height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = compute_triangle_area(sample_base, sample_height)
    print(result)