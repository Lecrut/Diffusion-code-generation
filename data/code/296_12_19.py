def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    initial_num = 10
    initial_den = 5
    simplified_ratio = simplify_fraction(initial_num, initial_den)
    print(f"Simplified ratio: {simplified_ratio[0]}/{simplified_ratio[1]}")