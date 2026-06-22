import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    side_a = 2
    side_b = 3
    area_a = hexagon_area(side_a)
    area_b = hexagon_area(side_b)
    total_area = area_a + area_b
    print(f"Area of Hexagon A with side {side_a}: {area_a}")
    print(f"Area of Hexagon B with side {side_b}: {area_b}")
    print(f"Total Area: {total_area}")