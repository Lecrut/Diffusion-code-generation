def trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

if __name__ == '__main__':
    b1 = 5
    b2 = 7
    h = 4
    area = trapezoid_area(b1, b2, h)
    print(area)