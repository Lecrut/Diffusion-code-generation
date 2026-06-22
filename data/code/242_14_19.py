import math
HEXAGON_SIDE = 5
PENTAGON_SIDE = 4

def hexagon_area(side):
    return 3 * math.sqrt(3) / 2 * pow(side, 2)

def pentagon_area(side):
    return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(side, 2)
if __name__ == '__main__':
    hex_area = hexagon_area(HEXAGON_SIDE)
    pent_area = pentagon_area(PENTAGON_SIDE)
    difference = abs(hex_area - pent_area)
    print(f'Absolute difference between hexagon and pentagon areas: {difference}')