class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = self._compute_gcd(num1, num2)
        return (num1 // gcd, num2 // gcd)

    def _compute_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result1 = calculator.simplify_ratio(48, 18)
    print("Simplified ratio of 48 to 18:", result1)
    
    result2 = calculator.simplify_ratio(100, 25)
    print("Simplified ratio of 100 to 25:", result2)
    
    result3 = calculator.simplify_ratio(7, 3)
    print("Simplified ratio of 7 to 3:", result3)