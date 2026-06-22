def trapezoid_area(base_a, base_b, height):
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("All dimensions must be non-negative")
    if base_a == 0 and base_b == 0 and height == 0:
        return 0.0
    return (base_a + base_b) * height / 2

if __name__ == '__main__':
    b1 = 10.0
    b2 = 15.0
    h = 7.0
    area = trapezoid_area(b1, b2, h)
    print(area)