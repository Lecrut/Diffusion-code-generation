import math

class ShapeAreaCalculator:
    def __init__(self):
        self.hexagon_side_length = 4
        self.circle_radius = 3

    def calculate_hexagon_area(self):
        return (3 * math.sqrt(3) / 2) * self.hexagon_side_length ** 2

    def calculate_circle_area(self):
        return math.pi * self.circle_radius ** 2

if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    hexagon_area = calculator.calculate_hexagon_area()
    circle_area = calculator.calculate_circle_area()
    print(f"Hexagon Side Length: {calculator.hexagon_side_length}")
    print(f"Calculated Hexagon Area: {hexagon_area}")
    print("-" * 30)
    print(f"Circle Radius: {calculator.circle_radius}")
    print(f"Calculated Circle Area: {circle_area}")