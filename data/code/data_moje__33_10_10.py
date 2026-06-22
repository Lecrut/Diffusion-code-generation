def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric.")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return (base * height) / 2

if __name__ == '__main__':
    result = calculate_triangle_area(10, 5)
    print(result)