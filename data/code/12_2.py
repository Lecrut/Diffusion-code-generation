import math
class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        if ratio_a == 0 and ratio_b == 0:
            return 0, 0
        a = abs(ratio_a)
        b = abs(ratio_b)
        if a == 0:
            return 0, 1 if b != 0 else 0
        if b == 0:
            return 1, 0
        common_divisor = math.gcd(a, b)
        simplified_a = a // common_divisor
        simplified_b = b // common_divisor
        if ratio_a < 0:
            simplified_a = -simplified_a
        if ratio_b < 0:
            simplified_b = -simplified_b
        return simplified_a, simplified_b
if __name__ == '__main__':
    converter = RatioConverter()
    ratio1_a = 12
    ratio1_b = 18
    s1_a, s1_b = converter.simplify(ratio1_a, ratio1_b)
    print(f"Simplifying ({ratio1_a}, {ratio1_b}): ({s1_a}, {s1_b})")
    ratio2_a = 25
    ratio2_b = 50
    s2_a, s2_b = converter.simplify(ratio2_a, ratio2_b)
    print(f"Simplifying ({ratio2_a}, {ratio2_b}): ({s2_a}, {s2_b})")
    ratio3_a = -100
    ratio3_b = 75
    s3_a, s3_b = converter.simplify(ratio3_a, ratio3_b)
    print(f"Simplifying ({ratio3_a}, {ratio3_b}): ({s3_a}, {s3_b})")
    ratio4_a = 10
    ratio4_b = 10
    s4_a, s4_b = converter.simplify(ratio4_a, ratio4_b)
    print(f"Simplifying ({ratio4_a}, {ratio4_b}): ({s4_a}, {s4_b})")
    ratio5_a = 0
    ratio5_b = 0
    s5_a, s5_b = converter.simplify(ratio5_a, ratio5_b)
    print(f"Simplifying ({ratio5_a}, {ratio5_b}): ({s5_a}, {s5_b})")
    ratio6_a = 17
    ratio6_b = 34
    s6_a, s6_b = converter.simplify(ratio6_a, ratio6_b)
    print(f"Simplifying ({ratio6_a}, {ratio6_b}): ({s6_a}, {s6_b})")