class RatioHandler:

    def simplify(self, numerator, denominator):
        gcd = self._gcd(numerator, denominator)
        return (numerator // gcd, denominator // gcd)

    def calculate_ratio(self, num1, den1, num2, den2):
        simplified_num1, simplified_den1 = self.simplify(num1, den1)
        simplified_num2, simplified_den2 = self.simplify(num2, den2)
        return (simplified_num1 * simplified_den2, simplified_den1 * simplified_num2)

    def _gcd(self, a, b):
        while b:
            a, b = (b, a % b)
        return a
if __name__ == '__main__':
    handler = RatioHandler()
    print(handler.simplify(8, 4))
    print(handler.calculate_ratio(1, 2, 3, 4))