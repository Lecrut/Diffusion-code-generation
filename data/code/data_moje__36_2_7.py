def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 10.0
    b2 = 6.0
    h = 5.0
    area = calculate_trapezoid_area(b1, b2, h)
    print(area)