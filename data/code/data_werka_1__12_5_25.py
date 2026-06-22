import math

def simplify_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        return (0, 0)
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    sample_values = [
        (10, 20),
        (0, 5),
        (7, 0),
        (0, 0),
        (36, 60)
    ]
    
    for num, denom in sample_values:
        simplified = simplify_ratio(num, denom)
        print(f"Simplified ratio of ({num}, {denom}) is: {simplified}")