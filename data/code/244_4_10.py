import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2

if __name__ == '__main__':
    hexagon_1 = Hexagon(2)
    hexagon_2 = Hexagon(3)

    area_1 = hexagon_1.area()
    area_2 = hexagon_2.area()

    total_area = area_1 + area_2

    print(f"Area of Hexagon 1 with side length 2: {area_1}")
    print(f"Area of Hexagon 2 with side length 3: {area_2}")
    print(f"Total Area of both hexagons: {total_area}")