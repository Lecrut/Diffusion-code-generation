def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    a = 5.0
    b = 7.0
    h = 4.0
    result = calculate_trapezoid_area(a, b, h)
    print(result)