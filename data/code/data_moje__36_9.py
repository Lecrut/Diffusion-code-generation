def compute_trapezoid_area(base_a, base_b, height):
    return 0.5 * (base_a + base_b) * height

if __name__ == '__main__':
    base1 = 5.0
    base2 = 7.0
    height = 3.0
    area = compute_trapezoid_area(base1, base2, height)
    print(area)