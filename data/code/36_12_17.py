def trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 5.0
    b2 = 7.0
    h = 4.0
    area = trapezoid_area(b1, b2, h)
    print(area)