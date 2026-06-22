def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 10
    b2 = 6
    h = 4
    print(trapezoid_area(b1, b2, h))