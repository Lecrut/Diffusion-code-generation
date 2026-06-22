import math

def simplify_ratio(numerator, denominator):
    common_divisor = math.gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == '__main__':
    initial_num = 10
    initial_den = 15
    simplified_num, simplified_den = simplify_ratio(initial_num, initial_den)
    print(f"Initial Ratio: {initial_num}/{initial_den}, Simplified Ratio: {simplified_num}/{simplified_den}")