def calculate_triangle_area(base, height):
    try:
        if not isinstance(base, (float, int)) or not isinstance(height, (float, int)):
            raise TypeError("Both base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    test_base = 7.0
    test_height = 4.0
    area_result = calculate_triangle_area(test_base, test_height)
    if area_result is not None:
        print(area_result)