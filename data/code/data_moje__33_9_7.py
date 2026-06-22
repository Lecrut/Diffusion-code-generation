def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        try:
            base = float(base)
        except (ValueError, TypeError):
            raise ValueError("Base must be a number or convertible to a number")
    if not isinstance(height, (int, float)):
        try:
            height = float(height)
        except (ValueError, TypeError):
            raise ValueError("Height must be a number or convertible to a number")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    print(compute_triangle_area(10, 5))
    print(compute_triangle_area("7.5", 4))
    print(compute_triangle_area(3.14, 2))