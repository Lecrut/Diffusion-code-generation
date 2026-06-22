def calculate_trapezoid_area(base_a, base_b, height):
    return ((base_a + base_b) * height) / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 20
    height_val = 5
    area_result = calculate_trapezoid_area(base1, base2, height_val)
    print(area_result)
    base3 = 7
    base4 = 3
    height_val2 = 4
    area_result2 = calculate_trapezoid_area(base3, base4, height_val2)
    print(area_result2)