def calculate_trapezoid_area(base1, base2, height):
    return ((base1 + base2) / 2) * height

if __name__ == '__main__':
    base_a = 5
    base_b = 9
    height_val = 4
    area_result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(area_result)