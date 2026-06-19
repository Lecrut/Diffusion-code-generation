import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        gcd = math.gcd(num1, num2)
        simplified_num1 = num1 // gcd
        simplified_num2 = num2 // gcd
        return (simplified_num1, simplified_num2)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(48, 60)
    print(result)