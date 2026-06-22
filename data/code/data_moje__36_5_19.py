def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    b1 = 10.0
    b2 = 6.0
    h = 4.0
    area = trapezoid_area(b1, b2, h)
    print(area)