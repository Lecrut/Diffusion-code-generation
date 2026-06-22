def simplify_fraction(numerator, denominator):
    gcd = 2
    while gcd <= min(numerator, denominator):
        if numerator % gcd == 0 and denominator % gcd == 0:
            numerator //= gcd
            denominator //= gcd
        else:
            gcd += 1
    return numerator, denominator

def are_fractions_equivalent(frac1, frac2):
    num1, den1 = simplify_fraction(*frac1)
    num2, den2 = simplify_fraction(*frac2)
    return (num1 == num2) and (den1 == den2)

if __name__ == '__main__':
    fraction1 = (3, 4)
    fraction2 = (6, 8)
    print(f"Fraction 1: {fraction1}")
    print(f"Fraction 2: {fraction2}")
    result = are_fractions_equivalent(fraction1, fraction2)
    print(f"Are the fractions equivalent? {result}")