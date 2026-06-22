def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def are_fractions_equivalent(fraction1, fraction2):
    simplified1 = simplify_fraction(*fraction1)
    simplified2 = simplify_fraction(*fraction2)
    return simplified1 == simplified2
if __name__ == '__main__':
    fraction1 = (3, 4)
    fraction2 = (6, 8)
    result = are_fractions_equivalent(fraction1, fraction2)
    print(result)