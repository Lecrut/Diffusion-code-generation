def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2.0

if __name__ == '__main__':
    base1 = 5.0
    base2 = 7.0
    height = 4.0
    result = trapezoid_area(base1, base2, height)
    print(result)