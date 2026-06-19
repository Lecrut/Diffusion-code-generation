import math

class WeightRatioConverter:

    @staticmethod
    def simplify(ratio1, ratio2):
        scaled_ratio1 = int(ratio1 * 1000)
        scaled_ratio2 = int(ratio2 * 1000)
        gcd = math.gcd(scaled_ratio1, scaled_ratio2)
        simplified_ratio1 = scaled_ratio1 // gcd
        simplified_ratio2 = scaled_ratio2 // gcd
        return (simplified_ratio1, simplified_ratio2)
if __name__ == '__main__':
    sample_value1 = 4.5
    sample_value2 = 2.25
    result = WeightRatioConverter.simplify(sample_value1, sample_value2)
    print(result)