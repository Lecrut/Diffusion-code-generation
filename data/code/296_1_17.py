import math

def simplify_ratio(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd

if __name__ == '__main__':
    num1 = 20
    den1 = 35
    simplified_num1, simplified_den1 = simplify_ratio(num1, den1)
    print(f"Simplified Ratio: {simplified_num1}/{simplified_den1}")

    num2 = 48
    den2 = 60
    simplified_num2, simplified_den2 = simplify_ratio(num2, den2)
    print(f"Simplified Ratio: {simplified_num2}/{simplified_den2}")