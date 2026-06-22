def compute_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    b1 = 10
    b2 = 20
    h = 5
    area = compute_trapezoid_area(b1, b2, h)
    print(area)