def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")
    return float((base * height) / 2)

if __name__ == '__main__':
    base = 10
    height = 5
    result = calculate_triangle_area(base, height)
    print(result)