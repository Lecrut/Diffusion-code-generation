import math

class RatioSimplifier:
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    @classmethod
    def simplify_ratio(cls, numerator, denominator):
        common_divisor = cls.gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    num1, den1 = 48, 60
    result_num, result_den = RatioSimplifier.simplify_ratio(num1, den1)
    print(f"Simplified Ratio: {result_num}/{result_den}")