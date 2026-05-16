import math
class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        if ratio_a == 0 and ratio_b == 0:
            return 0, 0
        if ratio_a == 0:
            return 0, 1
        if ratio_b == 0:
            return 1, 0
        gcd = math.gcd(abs(ratio_a), abs(ratio_b))
        simplified_a = ratio_a // gcd
        simplified_b = ratio_b // gcd
        if simplified_a < 0:
            simplified_a = -simplified_a
            simplified_b = -simplified_b
        return simplified_a, simplified_b
if __name__ == '__main__':
    converter = RatioConverter()
    ratio1_a = 12
    ratio1_b = 18
    simplified1_a, simplified1_b = converter.simplify(ratio1_a, ratio1_b)
    print(f"Simplifying {ratio1_a}:{ratio1_b} -> {simplified1_a}:{simplified1_b}")
    ratio2_a = 48
    ratio2_b = 18
    simplified2_a, simplified2_b = converter.simplify(ratio2_a, ratio2_b)
    print(f"Simplifying {ratio2_a}:{ratio2_b} -> {simplified2_a}:{simplified2_b}")
    ratio3_a = -30
    ratio3_b = 42
    simplified3_a, simplified3_b = converter.simplify(ratio3_a, ratio3_b)
    print(f"Simplifying {ratio3_a}:{ratio3_b} -> {simplified3_a}:{simplified3_b}")
    ratio4_a = 1000000
    ratio4_b = 500000
    simplified4_a, simplified4_b = converter.simplify(ratio4_a, ratio4_b)
    print(f"Simplifying {ratio4_a}:{ratio4_b} -> {simplified4_a}:{simplified4_b}")
    ratio5_a = 7
    ratio5_b = 5
    simplified5_a, simplified5_b = converter.simplify(ratio5_a, ratio5_b)
    print(f"Simplifying {ratio5_a}:{ratio5_b} -> {simplified5_a}:{simplified5_b}")
    ratio6_a = 0
    ratio6_b = 10
    simplified6_a, simplified6_b = converter.simplify(ratio6_a, ratio6_b)
    print(f"Simplifying {ratio6_a}:{ratio6_b} -> {simplified6_a}:{simplified6_b}")
    ratio7_a = 0
    ratio7_b = 0
    simplified7_a, simplified7_b = converter.simplify(ratio7_a, ratio7_b)
    print(f"Simplifying {ratio7_a}:{ratio7_b} -> {simplified7_a}:{simplified7_b}")