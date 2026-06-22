import math

def simplify_ratio(numerator, denominator):
    common_divisor = math.gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    ratios = {
        (10, 15): 4,
        (20, 7): 2
    }
    
    for (numerator, denominator), scale in ratios.items():
        result_num, result_den = simplify_ratio(numerator, denominator)
        print(f"Initial Ratio: {numerator}/{denominator}, Scale Factor: {scale}")
        print(f"Simplified Ratio: {result_num}/{result_den}")