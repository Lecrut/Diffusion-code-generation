import math

def hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

if __name__ == '__main__':
    try:
        side_a = 2
        side_b = 3
        area_a = hexagon_area(side_a)
        area_b = hexagon_area(side_b)
        total_area = area_a + area_b
        print(f"Side length of Hexagon A: {side_a}, Area: {area_a}")
        print(f"Side length of Hexagon B: {side_b}, Area: {area_b}")
        print(f"Total Area: {total_area}")
    except Exception as e:
        print(f"An error occurred: {e}")