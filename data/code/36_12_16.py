def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    b1 = 10.5
    b2 = 7.25
    h = 4.0
    area = calculate_trapezoid_area(b1, b2, h)
    print(area)