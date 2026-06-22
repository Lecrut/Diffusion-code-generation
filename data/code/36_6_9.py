def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1 = 10.0
    base2 = 6.0
    height = 5.0
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)