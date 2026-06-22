class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        if num2 == 0:
            raise ValueError("num2 cannot be zero")
        gcd_value = self._gcd(num1, num2)
        simplified_num1 = num1 // gcd_value
        simplified_num2 = num2 // gcd_value
        return (simplified_num1, simplified_num2)

    def _gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return abs(a)

if __name__ == '__main__':
    calculator = RatioCalculator()
    result = calculator.simplify_ratio(72, 96)
    print(result)