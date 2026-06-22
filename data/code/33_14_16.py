def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    result = calculate_triangle_area(10, 5)
    print(result)
    result2 = calculate_triangle_area(7.5, 3.2)
    print(result2)
    result3 = calculate_triangle_area(0, 10)
    print(result3)