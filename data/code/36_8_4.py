def calculate_trapezoid_area(base_a, base_b, height):
    if base_a < 0 or base_b < 0 or height < 0:
        raise ValueError("Bases and height must be non-negative.")
    return 0.5 * (base_a + base_b) * height

if __name__ == '__main__':
    base_1 = 5
    base_2 = 7
    height_1 = 4
    area = calculate_trapezoid_area(base_1, base_2, height_1)
    print(area)