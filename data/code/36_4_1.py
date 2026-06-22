def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1 = 10
    base2 = 8
    height = 5
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)