import math

class ShapeComparison:
    def __init__(self):
        self.hexagon_side = 4
        self.circle_radius = 3

    def calculate_hexagon_area(self):
        return (3 * math.sqrt(3) / 2) * self.hexagon_side ** 2

    def calculate_circle_area(self):
        return math.pi * self.circle_radius ** 2

if __name__ == '__main__':
    comparison = ShapeComparison()
    hexagon_area = comparison.calculate_hexagon_area()
    circle_area = comparison.calculate_circle_area()
    print("--- Area Comparison ---")
    print(f"Hexagon Side Length: {comparison.hexagon_side}")
    print(f"Calculated Hexagon Area: {hexagon_area:.6f}")
    print("-" * 30)
    print(f"Circle Radius: {comparison.circle_radius}")
    print(f"Calculated Circle Area: {circle_area:.6f}")