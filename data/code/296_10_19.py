def simplify_ratio(numerator, denominator):
    gcd = numerator
    while denominator % gcd != 0:
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

if __name__ == '__main__':
    print(simplify_ratio(45, 90))