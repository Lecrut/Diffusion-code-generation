import math
SHAPE_NAMES = {'hexagon': 'Regular Hexagon', 'circle': 'Circle'}

def calculate_hexagon_area(side_length):
    return 3 * math.sqrt(3) / 2 * side_length ** 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2
if __name__ == '__main__':
    hexagon_side_length = 4
    circle_radius = 3
    hexagon_area = calculate_hexagon_area(hexagon_side_length)
    circle_area = calculate_circle_area(circle_radius)
    print('--- Shape Area Comparison ---')
    print(f'{SHAPE_NAMES['hexagon']} Side Length: {hexagon_side_length}')
    print(f'Calculated {SHAPE_NAMES['hexagon']} Area: {hexagon_area:.2f}')
    print('-' * 30)
    print(f'{SHAPE_NAMES['circle']} Radius: {circle_radius}')
    print(f'Calculated {SHAPE_NAMES['circle']} Area: {circle_area:.2f}')