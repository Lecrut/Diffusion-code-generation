from math import gcd

CONVERSION_FACTOR = 1000

class WeightRatioConverter:
    @staticmethod
    def simplify(weight1, weight2):
        scaled_weight1 = int(weight1 * CONVERSION_FACTOR)
        scaled_weight2 = int(weight2 * CONVERSION_FACTOR)
        common_divisor = gcd(scaled_weight1, scaled_weight2)
        simplified_weight1 = scaled_weight1 // common_divisor
        simplified_weight2 = scaled_weight2 // common_divisor
        return (simplified_weight1, simplified_weight2)

if __name__ == '__main__':
    sample_weight1 = 4.5
    sample_weight2 = 2.25
    result = WeightRatioConverter.simplify(sample_weight1, sample_weight2)
    print(result)