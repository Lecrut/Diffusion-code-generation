import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        gcd = math.gcd(num1, num2)
        return (num1 // gcd, num2 // gcd)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(48, 60)
    print(result)