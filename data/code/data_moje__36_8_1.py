def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 6
    height = 4
    area = trapezoid_area(base1, base2, height)
    print(area)