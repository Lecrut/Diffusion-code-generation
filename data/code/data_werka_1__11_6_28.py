from math import gcd

class GeometryCalculator:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def simplify_ratio(self):
        common_divisor = gcd(self.side_a, self.side_b)
        simplified_a = self.side_a // common_divisor
        simplified_b = self.side_b // common_divisor
        return (simplified_a, simplified_b)

if __name__ == '__main__':
    triangle = GeometryCalculator(6, 8)
    ratio = triangle.simplify_ratio()
    print(ratio)