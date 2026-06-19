from math import gcd

class WeightRatioConverter:
    @staticmethod
    def simplify(ratio1, ratio2):
        scaled_ratio1 = int(ratio1 * 1000)
        scaled_ratio2 = int(ratio2 * 1000)
        common_divisor = gcd(scaled_ratio1, scaled_ratio2)
        simplified_ratio1 = scaled_ratio1 // common_divisor
        simplified_ratio2 = scaled_ratio2 // common_divisor
        return (simplified_ratio1, simplified_ratio2)

if __name__ == '__main__':
    ratio1 = 4.5
    ratio2 = 2.25
    result = WeightRatioConverter.simplify(ratio1, ratio2)
    print(result)