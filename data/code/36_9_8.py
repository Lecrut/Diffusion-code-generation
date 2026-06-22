def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 20
    height = 15
    result = trapezoid_area(base1, base2, height)
    print(result)