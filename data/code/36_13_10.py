def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    area = trapezoid_area(5, 7, 4)
    print(area)