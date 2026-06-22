import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def pentagon_area(side_length):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2

if __name__ == '__main__':
    hexagon_side = 3
    pentagon_side = 2
    hex_area = hexagon_area(hexagon_side)
    pent_area = pentagon_area(pentagon_side)
    difference = abs(hex_area - pent_area)
    print(f"Absolute difference between hexagon and pentagon area: {difference}")