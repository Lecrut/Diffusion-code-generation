def calculate_trapezoid_area(base_a, base_b, height):
    return 0.5 * (base_a + base_b) * height

if __name__ == '__main__':
    base_1 = 10
    base_2 = 15
    height_val = 7
    area = calculate_trapezoid_area(base_1, base_2, height_val)
    print(area)