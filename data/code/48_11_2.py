import math

def calculate_rectangle_properties(width, height):
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

if __name__ == '__main__':
    width = 5.0
    height = 3.0
    perimeter, area = calculate_rectangle_properties(width, height)
    print(perimeter)
    print(area)