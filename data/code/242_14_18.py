import math

class Polygon:

    @staticmethod
    def area(side_length):
        if len == 3:
            return math.sqrt(3) / 4 * side_length ** 2
        elif len == 4:
            return side_length ** 2
        elif len == 5:
            return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2
        elif len == 6:
            return 3 * math.sqrt(3) / 2 * side_length ** 2
        else:
            raise ValueError('Unsupported number of sides')
if __name__ == '__main__':
    hexagon_side = 5
    pentagon_side = 4
    hexagon_area = Polygon.area(6, hexagon_side)
    pentagon_area = Polygon.area(5, pentagon_side)
    area_difference = abs(hexagon_area - pentagon_area)
    print(f'Area difference: {area_difference}')