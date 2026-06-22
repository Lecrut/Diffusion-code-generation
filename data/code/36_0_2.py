def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    b1 = 10
    b2 = 15
    h = 7
    area = calculate_trapezoid_area(b1, b2, h)
    print(area)