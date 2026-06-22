def trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError('Dimensions must be non-negative')
    area = (base1 + base2) / 2 * height
    return area
if __name__ == '__main__':
    base1 = 5.0
    base2 = 7.0
    height = 4.0
    area = trapezoid_area(base1, base2, height)
    print(area)