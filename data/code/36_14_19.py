def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 10.5
    base_b = 7.5
    h = 8.0
    area = calculate_trapezoid_area(base_a, base_b, h)
    print(area)