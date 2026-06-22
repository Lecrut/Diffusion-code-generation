def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 10
    b2 = 15
    h = 7
    result = calculate_trapezoid_area(b1, b2, h)
    print(result)