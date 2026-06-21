import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd_value = math.gcd(abs(numerator), abs(denominator))
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    return (simplified_numerator, simplified_denominator)
if __name__ == '__main__':
    test_cases = [{'numerator': 18, 'denominator': 24}, {'numerator': 0, 'denominator': 5}, {'numerator': 7, 'denominator': 0}, {'numerator': 0, 'denominator': 0}]
    for case in test_cases:
        result = simplify_weight_ratio(case['numerator'], case['denominator'])
        print(f"Numerator: {case['numerator']}, Denominator: {case['denominator']} => Simplified Ratio: {result}")