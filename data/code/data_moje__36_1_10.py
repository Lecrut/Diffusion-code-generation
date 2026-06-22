def compute_trapezoid_area(base1, base2, height):
    if height < 0 or base1 < 0 or base2 < 0:
        raise ValueError("Base and height values must be non-negative.")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base_a = 10
    base_b = 15
    height_val = 7
    result = compute_trapezoid_area(base_a, base_b, height_val)
    print(result)