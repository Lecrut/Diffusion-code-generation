import math
HEXAGON_SIDE_LENGTH = 4
CIRCLE_RADIUS = 3

def calculate_hexagon_area(side_length):
    return 3 * math.sqrt(3) / 2 * side_length ** 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    hexagon_area = calculate_hexagon_area(HEXAGON_SIDE_LENGTH)
    circle_area = calculate_circle_area(CIRCLE_RADIUS)
    print('--- Shape Area Comparison ---')
    print(f'Hexagon Side Length: {HEXAGON_SIDE_LENGTH}')
    print(f'Calculated Hexagon Area: {hexagon_area:.6f}')
    print('-' * 30)
    print(f'Circle Radius: {CIRCLE_RADIUS}')
    print(f'Calculated Circle Area: {circle_area:.6f}')