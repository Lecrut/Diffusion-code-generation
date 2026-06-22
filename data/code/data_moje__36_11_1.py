def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    b1 = 5
    b2 = 10
    h = 8
    print(trapezoid_area(b1, b2, h))