from math import gcd

class WeightRatioConverter:
    @staticmethod
    def _scale_and_gcd(weight1, weight2):
        scaled_weight1 = int(weight1 * 1000)
        scaled_weight2 = int(weight2 * 1000)
        common_divisor = gcd(scaled_weight1, scaled_weight2)
        return scaled_weight1 // common_divisor, scaled_weight2 // common_divisor

    @staticmethod
    def simplify(weight1, weight2):
        return WeightRatioConverter._scale_and_gcd(weight1, weight2)

if __name__ == '__main__':
    converter = WeightRatioConverter()
    sample_weight1 = 4.5
    sample_weight2 = 2.25
    result1 = converter.simplify(sample_weight1, sample_weight2)
    print(result1)
    result2 = converter.simplify(3.6, 1.8)
    print(result2)