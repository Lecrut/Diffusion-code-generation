def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_a = 5.0
    base_b = 7.0
    height_val = 3.0
    result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(result)