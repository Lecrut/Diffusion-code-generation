def calculate_trapezoid_area(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Base lengths and height must be positive numbers.")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    a = 5
    b = 7
    h = 4
    area = calculate_trapezoid_area(a, b, h)
    print(area)