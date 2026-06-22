import math
PI = math.pi
CIRCLE_RADIUS = 5
SQUARE_SIDE_LENGTH = 6

def calculate_circle_area(radius):
    return PI * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2
if __name__ == '__main__':
    circle_area = calculate_circle_area(CIRCLE_RADIUS)
    square_area = calculate_square_area(SQUARE_SIDE_LENGTH)
    print(f'Circle area: {circle_area}')
    print(f'Square area: {square_area}')
    if circle_area > square_area:
        print('The circle has a larger area.')
    else:
        print('The square has a larger area or both have the same area.')