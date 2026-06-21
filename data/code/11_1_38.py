import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(num1, num2)
        return (num1 // gcd, num2 // gcd)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(48, 64)
    print(result)