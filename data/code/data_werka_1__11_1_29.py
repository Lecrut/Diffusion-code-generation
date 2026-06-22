class RatioCalculator:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("num2 cannot be zero")
        divisor = self.gcd(num1, num2)
        return (num1 // divisor, num2 // divisor)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(48, 64)
    print(result)