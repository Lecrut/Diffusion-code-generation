def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 5.0
    b2 = 3.0
    h = 4.0
    area = trapezoid_area(b1, b2, h)
    print(area)