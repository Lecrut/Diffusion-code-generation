def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1 = 10
    base2 = 14
    height = 7
    result = trapezoid_area(base1, base2, height)
    print(result)