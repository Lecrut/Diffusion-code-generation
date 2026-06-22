def compute_trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

if __name__ == '__main__':
    b1 = 10
    b2 = 20
    h = 5
    area = compute_trapezoid_area(b1, b2, h)
    print(area)