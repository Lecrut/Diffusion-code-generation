from math import gcd

class WeightRatioConverter:
    @staticmethod
    def simplify(weight1, weight2):
        factor = 1000
        numerator = int(weight1 * factor)
        denominator = int(weight2 * factor)
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    weight1 = 4.5
    weight2 = 2.25
    result = WeightRatioConverter.simplify(weight1, weight2)
    print(result)