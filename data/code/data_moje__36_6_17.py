def calculate_trapezoid_area(base_a, base_b, height):
    return (base_a + base_b) * height / 2

if __name__ == '__main__':
    base_1 = 10
    base_2 = 20
    height_val = 5
    result = calculate_trapezoid_area(base_1, base_2, height_val)
    print(result)