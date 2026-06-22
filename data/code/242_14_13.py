import math

class Polygon:
    def __init__(self, side_length):
        self.side_length = side_length

    def area_hexagon(self):
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2

    def area_pentagon(self):
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length ** 2

if __name__ == '__main__':
    hexagon = Polygon(side_length=5)
    pentagon = Polygon(side_length=5)

    hexagon_area = hexagon.area_hexagon()
    pentagon_area = pentagon.area_pentagon()

    difference = abs(hexagon_area - pentagon_area)

    print(f"Area of Hexagon: {hexagon_area}")
    print(f"Area of Pentagon: {pentagon_area}")
    print(f"Absolute Difference in Areas: {difference}")