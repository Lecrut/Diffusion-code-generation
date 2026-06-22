def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise ValueError("Base must be a numeric type")
    if not isinstance(height, (int, float)) or isinstance(height, bool):
        raise ValueError("Height must be a numeric type")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)