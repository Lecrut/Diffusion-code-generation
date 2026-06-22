def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == '__main__':
    num_a = 12
    den_b = 18
    simplified_num, simplified_den = simplify_ratio(num_a, den_b)
    print(f"Simplified Ratio: {simplified_num}:{simplified_den}")