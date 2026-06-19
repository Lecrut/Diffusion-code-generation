from math import gcd

class GeometryCalculator:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_ratio(self):
        common_divisor = gcd(self.side_a, self.side_b)
        simplified_side_a = self.side_a // common_divisor
        simplified_side_b = self.side_b // common_divisor
        return (simplified_side_a, simplified_side_b)

if __name__ == '__main__':
    calculator = GeometryCalculator(18, 24)
    ratio = calculator.calculate_ratio()
    print(ratio)