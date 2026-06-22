def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 10
    base_b = 6
    height_val = 5
    area = calculate_trapezoid_area(base_a, base_b, height_val)
    print(area)