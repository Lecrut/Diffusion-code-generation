def calculate_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base_sample = 7.5
        height_sample = 4.2
        area_result = calculate_area(base_sample, height_sample)
        print(area_result)
    except ValueError as e:
        print(e)