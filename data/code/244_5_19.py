import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

def total_area():
    semicircle_rad = 4
    rectangle_w = 5
    rectangle_h = 8
    return semicircle_area(semicircle_rad) + rectangle_area(rectangle_w, rectangle_h)

if __name__ == '__main__':
    print(total_area())