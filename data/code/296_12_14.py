def simplify_fraction(fraction):
    num, den = fraction
    gcd = abs(num * den)
    while gcd > 0:
        if num % gcd == 0 and den % gcd == 0:
            break
        gcd -= 1
    return (num // gcd, den // gcd)

if __name__ == '__main__':
    print(simplify_fraction((8, 20)))