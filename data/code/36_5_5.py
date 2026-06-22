def compute_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base1 = 10.0
    base2 = 20.0
    height = 5.0
    area = compute_trapezoid_area(base1, base2, height)
    print(area)