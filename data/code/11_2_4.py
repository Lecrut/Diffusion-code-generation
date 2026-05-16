import math
class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        common_divisor = math.gcd(num1, num2)
        simplified_num1 = num1 // common_divisor
        simplified_num2 = num2 // common_divisor
        return simplified_num1, simplified_num2
if __name__ == '__main__':
    calculator = RatioCalculator()
    num1_sample = 48
    num2_sample = 18
    result_num1, result_num2 = calculator.simplify_ratio(num1_sample, num2_sample)
    print(f"Ratio of {num1_sample} to {num2_sample} simplified is {result_num1}:{result_num2}")
    num1_sample = 100
    num2_sample = 75
    result_num1, result_num2 = calculator.simplify_ratio(num1_sample, num2_sample)
    print(f"Ratio of {num1_sample} to {num2_sample} simplified is {result_num1}:{result_num2}")
    num1_sample = 12
    num2_sample = 12
    result_num1, result_num2 = calculator.simplify_ratio(num1_sample, num2_sample)
    print(f"Ratio of {num1_sample} to {num2_sample} simplified is {result_num1}:{result_num2}")