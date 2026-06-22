def calculate_trapezoid_area(base1, base2, height):
    if height < 0 or base1 < 0 or base2 < 0:
        raise ValueError("Dimensions must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 10
    base_b = 8
    h = 5
    area = calculate_trapezoid_area(base_a, base_b, h)
    print(area)