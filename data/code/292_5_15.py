def calculate_trapezoid_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    sample_base1 = 10
    sample_base2 = 8
    sample_leg1 = 6
    sample_leg2 = 4
    perimeter = calculate_trapezoid_perimeter(sample_base1, sample_base2, sample_leg1, sample_leg2)
    print(perimeter)