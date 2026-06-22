import math

def calculate_hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def compare_areas(hex1_side, hex2_side):
    area1 = calculate_hexagon_area(hex1_side)
    area2 = calculate_hexagon_area(hex2_side)
    epsilon = 1e-9
    return abs(area1 - area2) < epsilon

if __name__ == '__main__':
    print(f"Test 1 (Expected False): {compare_areas(2, 3)}")
    print(f"Test 2 (Expected True): {compare_areas(math.sqrt(6), math.sqrt(4))}")