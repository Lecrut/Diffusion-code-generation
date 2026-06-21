import math
WIDTH = 5.0
HEIGHT = 3.0

def calculate_rectangle_properties(width, height):
    perimeter = 2 * (width + height)
    area = width * height
    return (perimeter, area)
if __name__ == '__main__':
    perimeter, area = calculate_rectangle_properties(WIDTH, HEIGHT)
    print(f'Perimeter: {perimeter}')
    print(f'Area: {area}')