import math

class GeometryCalculator:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplified_ratio(self):
        gcd_value = self.gcd(self.side_a, self.side_b)
        return (self.side_a // gcd_value, self.side_b // gcd_value)

if __name__ == '__main__':
    triangle = GeometryCalculator(18, 24)
    ratio = triangle.simplified_ratio()
    print(ratio)