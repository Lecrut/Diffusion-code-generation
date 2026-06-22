def calculate_trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    sample_base1 = 10.0
    sample_base2 = 6.0
    sample_height = 4.0
    result = calculate_trapezoid_area(sample_base1, sample_base2, sample_height)
    print(result)