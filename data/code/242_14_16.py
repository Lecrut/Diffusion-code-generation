import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def pentagon_area(side_length):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2

if __name__ == '__main__':
    hex_side = 5
    pent_side = 4
    hex_area = hexagon_area(hex_side)
    pent_area = pentagon_area(pent_side)
    difference = abs(hex_area - pent_area)
    print(difference)