import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_values = [
        (100, 25),
        (0, 5),
        (5, 0),
        (0, 0),
        (48, 18)
    ]
    
    for numerator, denominator in sample_values:
        result = simplify_weight_ratio(numerator, denominator)
        print(f"Simplified ratio of {numerator}:{denominator} is {result[0]}:{result[1]}")