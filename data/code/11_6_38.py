from math import gcd

class RightTriangleRatio:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    @staticmethod
    def simplify_ratio(side1, side2):
        common_divisor = gcd(side1, side2)
        return (side1 // common_divisor, side2 // common_divisor)
    
    def get_simplified_ratio(self):
        return RightTriangleRatio.simplify_ratio(self.side1, self.side2)

if __name__ == '__main__':
    triangle = RightTriangleRatio(30, 45)
    ratio = triangle.get_simplified_ratio()
    print(ratio)