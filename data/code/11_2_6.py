import math
class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        common_divisor = math.gcd(num1, num2)
        simplified_num1 = num1 // common_divisor
        simplified_num2 = num2 // common_divisor
        return simplified_num1, simplified_num2
if __name__ == '__main__':
    calculator = RatioCalculator()
    num1 = 48
    num2 = 18
    simplified_num1, simplified_num2 = calculator.simplify_ratio(num1, num2)
    print(f"Ratio of {num1} to {num2} in lowest terms: {simplified_num1}:{simplified_num2}")
    num1 = 100
    num2 = 75
    simplified_num1, simplified_num2 = calculator.simplify_ratio(num1, num2)
    print(f"Ratio of {num1} to {num2} in lowest terms: {simplified_num1}:{simplified_num2}")
    num1 = 12
    num2 = 12
    simplified_num1, simplified_num2 = calculator.simplify_ratio(num1, num2)
    print(f"Ratio of {num1} to {num2} in lowest terms: {simplified_num1}:{simplified_num2}")