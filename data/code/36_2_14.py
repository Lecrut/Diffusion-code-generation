def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    base_a = 10
    base_b = 20
    height_val = 5
    result = calculate_trapezoid_area(base_a, base_b, height_val)
    print(result)