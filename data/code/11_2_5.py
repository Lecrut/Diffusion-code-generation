import math
class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        common_divisor = math.gcd(num1, num2)
        simplified_num1 = num1 // common_divisor
        simplified_num2 = num2 // common_divisor
        return simplified_num1, simplified_num2
if __name__ == '__main__':
    calculator = RatioCalculator()
    num1_a = 12
    num2_a = 18
    result_a = calculator.simplify_ratio(num1_a, num2_a)
    print(f"Ratio of {num1_a} to {num2_a} simplified: {result_a[0]}:{result_a[1]}")
    num1_b = 25
    num2_b = 100
    result_b = calculator.simplify_ratio(num1_b, num2_b)
    print(f"Ratio of {num1_b} to {num2_b} simplified: {result_b[0]}:{result_b[1]}")
    num1_c = 7
    num2_c = 3
    result_c = calculator.simplify_ratio(num1_c, num2_c)
    print(f"Ratio of {num1_c} to {num2_c} simplified: {result_c[0]}:{result_c[1]}")