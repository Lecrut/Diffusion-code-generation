def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    test_base1 = 10
    test_base2 = 6
    test_height = 4
    result = calculate_trapezoid_area(test_base1, test_base2, test_height)
    print(result)