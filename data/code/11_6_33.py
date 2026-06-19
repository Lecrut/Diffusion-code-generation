import math

class GeometryCalculator:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_ratio(self):
        common_divisor = self.gcd(self.side1, self.side2)
        simplified_side1 = self.side1 // common_divisor
        simplified_side2 = self.side2 // common_divisor
        return (simplified_side1, simplified_side2)

if __name__ == '__main__':
    triangle = GeometryCalculator(6, 8)
    ratio = triangle.simplify_ratio()
    print(ratio)