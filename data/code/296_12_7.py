def simplify_fraction(fraction):
    numerator, denominator = fraction
    gcd = abs(numerator * denominator)
    while gcd > 0:
        if numerator % gcd == 0 and denominator % gcd == 0:
            break
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

if __name__ == '__main__':
    print(simplify_fraction((8, 24)))