def calculate_area(base, height):
    try:
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    base_sample = 7.5
    height_sample = 4.2
    area_result = calculate_area(base_sample, height_sample)
    if area_result is not None:
        print(area_result)