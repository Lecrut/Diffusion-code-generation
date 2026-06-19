def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_weight_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    optimized_numerator = numerator // common_divisor
    optimized_denominator = denominator // common_divisor
    return optimized_numerator, optimized_denominator

if __name__ == '__main__':
    sample_numerator = 1000000000000
    sample_denominator = 2500000000000
    result = convert_weight_ratio(sample_numerator, sample_denominator)
    print(result)