def are_fractions_equivalent(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    gcd1 = gcd(num1, den1)
    num1 //= gcd1
    den1 //= gcd1
    gcd2 = gcd(num2, den2)
    num2 //= gcd2
    den2 //= gcd2
    return (num1, den1) == (num2, den2)

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a
if __name__ == '__main__':
    fraction1 = (3, 4)
    fraction2 = (6, 8)
    result = are_fractions_equivalent(fraction1, fraction2)
    print(result)
    fraction3 = (2, 3)
    fraction4 = (4, 7)
    result = are_fractions_equivalent(fraction3, fraction4)
    print(result)