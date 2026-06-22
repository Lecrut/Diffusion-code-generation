def trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

if __name__ == '__main__':
    result = trapezoid_area(5, 3, 4)
    print(result)