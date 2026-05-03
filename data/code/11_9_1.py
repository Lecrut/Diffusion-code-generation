import math
class TriangleCalculator:
    def calculate_side_ratio(self, a, b):
        common_divisor = math.gcd(a, b)
        ratio_a = a // common_divisor
        ratio_b = b // common_divisor
        return ratio_a, ratio_b
if __name__ == '__main__':
    calculator = TriangleCalculator()
    side1 = 12
    side2 = 18
    ratio1, ratio2 = calculator.calculate_side_ratio(side1, side2)
    print(f"Ratio of {side1} and {side2}: {ratio1}:{ratio2}")