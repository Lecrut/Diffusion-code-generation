import math

class WeightRatioConverter:
    @staticmethod
    def _calculate_gcd(a, b):
        return math.gcd(int(a), int(b))

    @staticmethod
    def convert_weight_ratios(weight1, weight2):
        gcd = WeightRatioConverter._calculate_gcd(weight1, weight2)
        return (int(weight1) // gcd, int(weight2) // gcd)

if __name__ == '__main__':
    sample_weight1 = 90.0
    sample_weight2 = 150.0
    converter = WeightRatioConverter()
    result = converter.convert_weight_ratios(sample_weight1, sample_weight2)
    print(result)