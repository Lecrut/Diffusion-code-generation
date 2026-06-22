def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base < 0:
        raise ValueError("Base cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)