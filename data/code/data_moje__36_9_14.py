def compute_trapezoid_area(base_a, base_b, height):
    return (base_a + base_b) * height / 2

if __name__ == '__main__':
    base1 = 5
    base2 = 9
    h = 4
    area = compute_trapezoid_area(base1, base2, h)
    print(area)