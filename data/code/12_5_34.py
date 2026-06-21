import math

def simplify_weight_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    
    gcd_value = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_weight1 = 45
    sample_weight2 = 60
    result = simplify_weight_ratio(sample_weight1, sample_weight2)
    print(result)