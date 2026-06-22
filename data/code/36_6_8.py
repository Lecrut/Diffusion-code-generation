def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 15
    height = 6
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)