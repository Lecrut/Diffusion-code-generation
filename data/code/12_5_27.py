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
        (48, 18)
    ]
    
    for num, denom in sample_values:
        result = simplify_weight_ratio(num, denom)
        print(f"Simplified ratio of {num}/{denom} is {result}")