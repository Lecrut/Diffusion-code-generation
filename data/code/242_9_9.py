import math

SEMICIRCLE_RADIUS = 4
RECTANGLE_WIDTH = 6
RECTANGLE_HEIGHT = 3

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    semicircle_a = semicircle_area(SEMICIRCLE_RADIUS)
    rectangle_a = rectangle_area(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
    print(f"Semicircle area: {semicircle_a:.10f}")
    print(f"Rectangle area: {rectangle_a:.10f}")