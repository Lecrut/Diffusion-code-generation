from math import gcd

class RightTriangle:
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Sides of the triangle must be positive numbers.")
        self.side_a = side_a
        self.side_b = side_b

    def simplify_ratio(self):
        common_divisor = gcd(self.side_a, self.side_b)
        return (self.side_a // common_divisor, self.side_b // common_divisor)

if __name__ == '__main__':
    try:
        triangle = RightTriangle(30, 45)
        ratio = triangle.simplify_ratio()
        print(ratio)
    except ValueError as e:
        print(e)