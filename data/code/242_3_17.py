import math

class ShapeAreas:
    HEXAGON_SIDE = 4
    CIRCLE_RADIUS = 3

    @staticmethod
    def hexagon_area(side):
        return (3 * math.sqrt(3) / 2) * side ** 2

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

if __name__ == '__main__':
    hexagon_area = ShapeAreas.hexagon_area(ShapeAreas.HEXAGON_SIDE)
    circle_area = ShapeAreas.circle_area(ShapeAreas.CIRCLE_RADIUS)
    
    print("--- Shape Area Comparison ---")
    print(f"Hexagon Side Length: {ShapeAreas.HEXAGON_SIDE}")
    print(f"Calculated Hexagon Area: {hexagon_area:.2f}")
    print("-" * 30)
    print(f"Circle Radius: {ShapeAreas.CIRCLE_RADIUS}")
    print(f"Calculated Circle Area: {circle_area:.2f}")