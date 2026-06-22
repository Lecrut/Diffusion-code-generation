import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 1)
    common_divisor = math.gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return (simplified_numerator, simplified_denominator)
if __name__ == '__main__':
    sample_numerators = [0, 12, 100, 56]
    sample_denominators = [0, 36, 80, 98]
    for num, denom in zip(sample_numerators, sample_denominators):
        simplified_ratio = simplify_weight_ratio(num, denom)
        print(f'Simplified ratio of ({num}, {denom}) is {simplified_ratio}')