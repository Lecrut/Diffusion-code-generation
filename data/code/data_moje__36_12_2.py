def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative")
    if not (base1 + base2):
        return 0.0
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 10.0
    base_b = 6.0
    height_val = 4.0
    result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(result)