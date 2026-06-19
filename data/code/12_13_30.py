class WeightRatioConverter:

    @staticmethod
    def simplify(ratio1, ratio2):
        import math
        num1 = int(ratio1 * 1000)
        num2 = int(ratio2 * 1000)
        gcd = math.gcd(num1, num2)
        simplified_num1 = num1 // gcd
        simplified_num2 = num2 // gcd
        return (simplified_num1, simplified_num2)
if __name__ == '__main__':
    sample_ratio1 = 4.5
    sample_ratio2 = 2.25
    result = WeightRatioConverter.simplify(sample_ratio1, sample_ratio2)
    print(result)