def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base and height values must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 10
    base_b = 15
    height_val = 8
    area_result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(area_result)