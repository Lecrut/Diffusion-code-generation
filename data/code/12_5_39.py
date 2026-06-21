import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        raise ValueError("Both numerator and denominator cannot be zero.")
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    try:
        sample_numerator = 48
        sample_denominator = 180
        result = simplify_weight_ratio(sample_numerator, sample_denominator)
        print(result)
    except ValueError as e:
        print(e)