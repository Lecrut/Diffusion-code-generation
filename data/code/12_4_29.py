def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def combine_ratios(A, B, C, D):
    combined_numerator = A * D
    combined_denominator = B * C
    simplified_numerator, simplified_denominator = simplify_ratio(combined_numerator, combined_denominator)
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    A, B, C, D = 4, 5, 6, 7
    result = combine_ratios(A, B, C, D)
    print(result)