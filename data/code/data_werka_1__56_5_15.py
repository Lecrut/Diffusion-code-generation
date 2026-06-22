import math
RECTANGLE_LENGTH = 6
RECTANGLE_WIDTH = 8
CIRCLE_DIAMETER = 10

def calculate_diagonal(length, width):
    return math.sqrt(length ** 2 + width ** 2)

def calculate_radius(diameter):
    return diameter / 2
if __name__ == '__main__':
    diagonal = calculate_diagonal(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    radius = calculate_radius(CIRCLE_DIAMETER)
    if radius != 0:
        ratio = diagonal / radius
        print(ratio)
    else:
        print('Undefined ratio (division by zero)')