def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    result = trapezoid_area(5, 10, 7)
    print(result)