import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    side_a = 4
    side_b = 5
    area_a = hexagon_area(side_a)
    area_b = hexagon_area(side_b)
    total_area = area_a + area_b
    print(f"Side length of Hexagon A: {side_a}")
    print(f"Side length of Hexagon B: {side_b}")
    print(f"Area of Hexagon A: {area_a:.2f}")
    print(f"Area of Hexagon B: {area_b:.2f}")
    print(f"Total Area: {total_area:.2f}")