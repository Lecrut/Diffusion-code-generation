def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    sample_base1 = 10
    sample_base2 = 6
    sample_height = 4
    result = trapezoid_area(sample_base1, sample_base2, sample_height)
    print(result)