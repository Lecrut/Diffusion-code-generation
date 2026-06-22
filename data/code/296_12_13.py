def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    simplified_num = numerator // common_divisor
    simplified_den = denominator // common_divisor
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    initial_num = 20
    initial_den = 8
    simplified_fraction = simplify_fraction(initial_num, initial_den)
    print(f"Simplified fraction: {simplified_fraction[0]}/{simplified_fraction[1]}")