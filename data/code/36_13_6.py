def calculate_trapezoid_area(base_a, base_b, height):
    return (base_a + base_b) * height / 2

if __name__ == '__main__':
    base1 = 10
    base2 = 20
    height = 5
    area = calculate_trapezoid_area(base1, base2, height)
    print(area)