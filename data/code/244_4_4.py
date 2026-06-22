import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    areas = {2: hexagon_area(2), 3: hexagon_area(3)}
    total_area = sum(areas.values())
    print(f"Total Area of Hexagons with sides 2 and 3: {total_area}")