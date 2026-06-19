class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("num2 cannot be zero")
        
        gcd = self._gcd(num1, num2)
        return (num1 // gcd, num2 // gcd)

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(48, 18)
    print(result)