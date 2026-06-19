import math

class GeometryCalculator:
    def calculate_ratio(self, side1, side2):
        gcd = math.gcd(side1, side2)
        simplified_side1 = side1 // gcd
        simplified_side2 = side2 // gcd
        return (simplified_side1, simplified_side2)

if __name__ == '__main__':
    calculator = GeometryCalculator()
    ratio = calculator.calculate_ratio(8, 12)
    print(ratio)