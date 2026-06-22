def calculate_trapezoid_area(base1, base2, height):
    if height < 0:
        raise ValueError("Height must be non-negative")
    if base1 < 0 or base2 < 0:
        raise ValueError("Base lengths must be non-negative")
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base_a = 10
    base_b = 20
    h = 5
    area = calculate_trapezoid_area(base_a, base_b, h)
    print(area)