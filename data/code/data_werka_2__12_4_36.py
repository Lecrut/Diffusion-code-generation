from math import gcd

class RatioCalculator:
    @staticmethod
    def simplify_ratio(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return numerator // common_divisor, denominator // common_divisor

    @staticmethod
    def calculate_equivalent_ratio(A, B, C, D):
        AD = A * D
        BC = B * C
        return RatioCalculator.simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 5, 6
    C, D = 7, 8
    result = RatioCalculator.calculate_equivalent_ratio(A, B, C, D)
    print(result)