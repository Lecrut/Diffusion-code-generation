from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def combine_ratios(A, B, C, D):
    combined_numerator = A * D
    combined_denominator = B * C
    simplified_ratio = simplify_ratio(combined_numerator, combined_denominator)
    return simplified_ratio
if __name__ == '__main__':
    A, B = (3, 4)
    C, D = (5, 6)
    result = combine_ratios(A, B, C, D)
    print(result)