import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2

if __name__ == '__main__':
    hexagon_2 = Hexagon(2)
    hexagon_3 = Hexagon(3)
    area_2 = hexagon_2.area()
    area_3 = hexagon_3.area()
    total_area = area_2 + area_3
    print(f"Area of Hexagon with side length 2: {area_2}")
    print(f"Area of Hexagon with side length 3: {area_3}")
    print(f"Total Area: {total_area}")