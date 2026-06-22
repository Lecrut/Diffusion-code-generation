def calculate_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base and height values must be non-negative")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base_a = 10.0
    base_b = 20.0
    height_val = 15.0
    result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(result)