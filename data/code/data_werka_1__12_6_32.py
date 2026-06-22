def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
if __name__ == '__main__':
    large_numerator = 12345678901234567890
    large_denominator = 98765432109876543210
    simplified_ratio = simplify_ratio(large_numerator, large_denominator)
    print(simplified_ratio)