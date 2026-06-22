import math

class WeightRatioConverter:

    @staticmethod
    def simplify(weight1, weight2):
        weight1 *= 1000
        weight2 *= 1000
        gcd = math.gcd(int(weight1), int(weight2))
        simplified_weight1 = int(weight1) // gcd
        simplified_weight2 = int(weight2) // gcd
        return (simplified_weight1, simplified_weight2)
if __name__ == '__main__':
    weight1 = 4.5
    weight2 = 2.25
    result = WeightRatioConverter.simplify(weight1, weight2)
    print(result)