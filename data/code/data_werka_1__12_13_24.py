class WeightRatioConverter:
    @staticmethod
    def simplify(ratio1, ratio2):
        import math
        scale = 1000
        num1 = int(ratio1 * scale)
        num2 = int(ratio2 * scale)
        gcd = math.gcd(num1, num2)
        return (num1 // gcd, num2 // gcd)

if __name__ == '__main__':
    ratio1 = 4.5
    ratio2 = 2.25
    result = WeightRatioConverter.simplify(ratio1, ratio2)
    print(result)