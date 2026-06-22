import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    hex_side = 4
    circ_radius = 3
    print(hexagon_area(hex_side))
    print(circle_area(circ_radius))