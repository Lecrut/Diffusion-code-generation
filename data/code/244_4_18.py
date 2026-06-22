import math
HEXAGON_AREA_FACTOR = 3 * math.sqrt(3) / 2

def calculate_hexagon_area(side_length):
    return HEXAGON_AREA_FACTOR * side_length ** 2
if __name__ == '__main__':
    side_length_a = 2
    side_length_b = 3
    area_a = calculate_hexagon_area(side_length_a)
    area_b = calculate_hexagon_area(side_length_b)
    total_area = area_a + area_b
    print(f'Area of hexagon with side length {side_length_a}: {area_a}')
    print(f'Area of hexagon with side length {side_length_b}: {area_b}')
    print(f'Total area: {total_area}')