import math

class GeometryCalculator:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_ratio(self):
        gcd_value = self.gcd(self.side_a, self.side_b)
        simplified_a = self.side_a // gcd_value
        simplified_b = self.side_b // gcd_value
        return (simplified_a, simplified_b)

if __name__ == '__main__':
    calculator = GeometryCalculator(18, 24)
    ratio = calculator.simplify_ratio()
    print(ratio)