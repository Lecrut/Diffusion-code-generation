import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    try:
        area_2 = hexagon_area(2)
        area_3 = hexagon_area(3)
        total_area = area_2 + area_3
        print(f"Total Area of Hexagons: {total_area}")
    except TypeError as e:
        print(f"Invalid input: {e}")