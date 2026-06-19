import math

class WeightRatioConverter:
    @staticmethod
    def simplify(weight1, weight2):
        factor = 1000
        w1 = int(weight1 * factor)
        w2 = int(weight2 * factor)
        gcd = math.gcd(w1, w2)
        return (w1 // gcd, w2 // gcd)

if __name__ == '__main__':
    weight1 = 4.5
    weight2 = 2.25
    result = WeightRatioConverter.simplify(weight1, weight2)
    print(result)