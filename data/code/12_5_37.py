import math

def validate_inputs(numerator, denominator):
    if numerator == 0 and denominator == 0:
        raise ValueError('Both numerator and denominator cannot be zero simultaneously.')

def simplify_weight_ratio(numerator, denominator):
    try:
        validate_inputs(numerator, denominator)
    except ValueError as e:
        print(e)
        return (0, 0)
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return (simplified_numerator, simplified_denominator)
if __name__ == '__main__':
    sample_numerator = 35
    sample_denominator = 49
    result = simplify_weight_ratio(sample_numerator, sample_denominator)
    print(result)
    try:
        result_zero_both = simplify_weight_ratio(0, 0)
        print(result_zero_both)
    except ValueError as e:
        print(e)
    result_zero_numerator = simplify_weight_ratio(0, 15)
    print(result_zero_numerator)
    result_zero_denominator = simplify_weight_ratio(20, 0)
    print(result_zero_denominator)