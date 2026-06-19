from math import gcd

class WeightRatioConverter:

    @staticmethod
    def simplify(weight1, weight2):
        weight1_int = int(weight1 * 1000)
        weight2_int = int(weight2 * 1000)
        common_divisor = gcd(weight1_int, weight2_int)
        simplified_weight1 = weight1_int // common_divisor
        simplified_weight2 = weight2_int // common_divisor
        return (simplified_weight1, simplified_weight2)
if __name__ == '__main__':
    sample_weight1 = 4.5
    sample_weight2 = 2.25
    result = WeightRatioConverter.simplify(sample_weight1, sample_weight2)
    print(result)