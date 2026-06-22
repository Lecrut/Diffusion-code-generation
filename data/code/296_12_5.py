def simplify_fraction(fraction):
    numerator, denominator = fraction
    gcd = abs(numerator) if numerator < 0 else numerator
    while gcd > 1:
        if numerator % gcd == 0 and denominator % gcd == 0:
            break
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

if __name__ == '__main__':
    print(simplify_fraction((8, 4)))