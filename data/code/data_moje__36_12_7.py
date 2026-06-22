def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    result = trapezoid_area(5.0, 7.0, 4.0)
    print(result)