def are_fractions_equivalent(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    return num1 * den2 == num2 * den1
if __name__ == '__main__':
    print(are_fractions_equivalent((1, 2), (2, 4)))
    print(are_fractions_equivalent((3, 4), (6, 8)))
    print(are_fractions_equivalent((1, 3), (2, 5)))