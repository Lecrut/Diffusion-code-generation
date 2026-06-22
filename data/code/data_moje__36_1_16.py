def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base lengths and height must be non-negative.")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1_value = 5.0
    base2_value = 7.0
    height_value = 10.0
    area = calculate_trapezoid_area(base1_value, base2_value, height_value)
    print(area)