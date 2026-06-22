def trapezoid_perimeter(base1, base2, leg1, leg2):
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    sample_base1 = 8.5
    sample_base2 = 6.2
    sample_leg1 = 3.7
    sample_leg2 = 4.9
    perimeter = trapezoid_perimeter(sample_base1, sample_base2, sample_leg1, sample_leg2)
    print(perimeter)