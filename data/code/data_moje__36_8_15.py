def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) / 2 * height

if __name__ == '__main__':
    base1 = 10.0
    base2 = 6.0
    height = 4.0
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)