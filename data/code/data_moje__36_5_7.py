def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 5
    base2 = 10
    height = 8
    area = trapezoid_area(base1, base2, height)
    print(area)