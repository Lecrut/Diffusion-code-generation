def trapezoid_area(base_a, base_b, height):
    return 0.5 * (base_a + base_b) * height

if __name__ == '__main__':
    base_a = 5
    base_b = 10
    height = 4
    result = trapezoid_area(base_a, base_b, height)
    print(result)