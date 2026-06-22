def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    BASE_SAMPLE = 8.1
    HEIGHT_SAMPLE = 5.4
    area_result = calculate_area(BASE_SAMPLE, HEIGHT_SAMPLE)
    print(area_result)