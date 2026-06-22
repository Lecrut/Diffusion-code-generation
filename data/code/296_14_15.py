def is_fraction_equivalent(frac1, frac2):
    num1, denom1 = frac1
    num2, denom2 = frac2

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcd1 = gcd(num1, denom1)
    num1 //= gcd1
    denom1 //= gcd1
    gcd2 = gcd(num2, denom2)
    num2 //= gcd2
    denom2 //= gcd2
    return num1 == num2 and denom1 == denom2
if __name__ == '__main__':
    frac1 = (4, 8)
    frac2 = (2, 4)
    result = is_fraction_equivalent(frac1, frac2)
    print(result)
    frac3 = (3, 4)
    frac4 = (5, 6)
    result = is_fraction_equivalent(frac3, frac4)
    print(result)