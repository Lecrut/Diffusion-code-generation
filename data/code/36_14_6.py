def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    a = 5
    b = 7
    h = 4
    area = trapezoid_area(a, b, h)
    print(area)