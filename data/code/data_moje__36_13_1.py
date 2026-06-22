def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 5
    base_b = 7
    height_val = 4
    area = calculate_trapezoid_area(base_a, base_b, height_val)
    print(area)