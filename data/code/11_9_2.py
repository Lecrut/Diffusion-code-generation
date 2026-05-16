import math
class TriangleCalculator:
    def calculate_side_ratio(self, side_a, side_b):
        gcd_value = math.gcd(side_a, side_b)
        ratio_a = side_a // gcd_value
        ratio_b = side_b // gcd_value
        return ratio_a, ratio_b
if __name__ == '__main__':
    calculator = TriangleCalculator()
    side1 = 12
    side2 = 18
    ratio1, ratio2 = calculator.calculate_side_ratio(side1, side2)
    print(f"Ratio of {side1} and {side2}: {ratio1}:{ratio2}")