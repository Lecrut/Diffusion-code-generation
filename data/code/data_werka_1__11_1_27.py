class RatioCalculator:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("Denominator cannot be zero")
        common_divisor = self.gcd(num1, num2)
        simplified_num1 = num1 // common_divisor
        simplified_num2 = num2 // common_divisor
        return (simplified_num1, simplified_num2)

if __name__ == '__main__':
    calculator = RatioCalculator()
    ratio = calculator.simplify_ratio(48, 60)
    print(ratio)