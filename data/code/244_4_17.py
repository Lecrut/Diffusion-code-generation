import math

class Hexagon:
    @staticmethod
    def area(side_length):
        return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    area_2 = Hexagon.area(2)
    area_3 = Hexagon.area(3)
    total_area = area_2 + area_3
    print(total_area)