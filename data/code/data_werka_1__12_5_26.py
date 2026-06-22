import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_numerator = 12
    sample_denominator = 18
    result = simplify_weight_ratio(sample_numerator, sample_denominator)
    print(result)