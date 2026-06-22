def compute_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 10.0
    b2 = 20.0
    h = 8.0
    area = compute_trapezoid_area(b1, b2, h)
    print(area)