def trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2.0 * height

if __name__ == '__main__':
    b1 = 5.0
    b2 = 10.0
    h = 4.0
    result = trapezoid_area(b1, b2, h)
    print(result)