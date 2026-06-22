from math import gcd

def calculate_simplified_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_numerator = 1000000000
    sample_denominator = 500000000
    result = calculate_simplified_ratio(sample_numerator, sample_denominator)
    print(result)