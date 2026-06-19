import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd_value = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_values = [
        (100, 25),
        (0, 5),
        (7, 0),
        (0, 0),
        (36, 12),
        (81, 9)
    ]
    
    for numerator, denominator in sample_values:
        result = simplify_weight_ratio(numerator, denominator)
        print(f"Simplified ratio of {numerator}:{denominator} is {result}")