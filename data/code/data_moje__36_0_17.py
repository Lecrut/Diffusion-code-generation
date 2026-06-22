def trapezoid_area(b1, b2, height):
    return 0.5 * (b1 + b2) * height

if __name__ == '__main__':
    base1 = 10.0
    base2 = 6.0
    height = 4.0
    print(trapezoid_area(base1, base2, height))