def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    sample_base1 = 5
    sample_base2 = 7
    sample_height = 4
    result = calculate_trapezoid_area(sample_base1, sample_base2, sample_height)
    print(result)