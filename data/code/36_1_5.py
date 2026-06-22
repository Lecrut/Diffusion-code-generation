def compute_trapezoid_area(base_a, base_b, height):
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative.")
    return 0.5 * (base_a + base_b) * height

if __name__ == '__main__':
    base1 = 10
    base2 = 14
    h = 5
    area = compute_trapezoid_area(base1, base2, h)
    print(area)