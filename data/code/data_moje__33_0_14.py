def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric types.")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

if __name__ == '__main__':
    print(calculate_triangle_area(10, 5))
    print(calculate_triangle_area(7.5, 3.2))