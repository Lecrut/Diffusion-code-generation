import math

class GeometryCalculator:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplified_ratio(self):
        gcd_value = self.gcd(self.side1, self.side2)
        return (self.side1 // gcd_value, self.side2 // gcd_value)

if __name__ == '__main__':
    triangle = GeometryCalculator(6, 8)
    print(triangle.simplified_ratio())