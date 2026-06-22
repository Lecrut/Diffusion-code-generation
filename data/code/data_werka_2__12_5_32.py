import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        raise ValueError("Both numerator and denominator cannot be zero.")
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

if __name__ == '__main__':
    sample_numerator = 18
    sample_denominator = 24
    simplified_ratio = simplify_weight_ratio(sample_numerator, sample_denominator)
    print(simplified_ratio)