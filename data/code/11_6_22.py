from math import gcd

class TriangleCalculator:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def simplify_ratio(self):
        common_divisor = gcd(self.side1, self.side2)
        return self.side1 // common_divisor, self.side2 // common_divisor

if __name__ == '__main__':
    triangle = TriangleCalculator(8, 12)
    simplified_ratio = triangle.simplify_ratio()
    print(simplified_ratio)