from math import gcd

class WeightRatioConverter:

    @staticmethod
    def simplify(ratio1, ratio2):
        num1 = int(ratio1 * 1000)
        num2 = int(ratio2 * 1000)
        common_divisor = gcd(num1, num2)
        simplified_num1 = num1 // common_divisor
        simplified_num2 = num2 // common_divisor
        return (simplified_num1, simplified_num2)
if __name__ == '__main__':
    sample_ratio1 = 4.5
    sample_ratio2 = 2.25
    result = WeightRatioConverter.simplify(sample_ratio1, sample_ratio2)
    print(result)