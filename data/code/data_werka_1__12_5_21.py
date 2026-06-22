import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd_value = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_numerator = 18
    sample_denominator = 24
    result = simplify_weight_ratio(sample_numerator, sample_denominator)
    print(result)