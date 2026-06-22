import math
HEXAGON_AREA_FACTOR = 3 * math.sqrt(3) / 2

def calculate_hexagon_area(side_length):
    return HEXAGON_AREA_FACTOR * side_length ** 2
if __name__ == '__main__':
    area_2 = calculate_hexagon_area(2)
    area_3 = calculate_hexagon_area(3)
    total_area = area_2 + area_3
    print(total_area)