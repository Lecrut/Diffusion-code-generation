import math

class WeightRatioConverter:
    @staticmethod
    def simplify(ratio1, ratio2):
        scaled_ratio1 = int(ratio1 * 1000)
        scaled_ratio2 = int(ratio2 * 1000)
        gcd = math.gcd(scaled_ratio1, scaled_ratio2)
        return (scaled_ratio1 // gcd, scaled_ratio2 // gcd)

if __name__ == '__main__':
    ratio1 = 4.5
    ratio2 = 2.25
    simplified_ratio = WeightRatioConverter.simplify(ratio1, ratio2)
    print(simplified_ratio)