import math

def semicircle_area(radius):
    return 0.5 * math.pi * radius ** 2

def rectangle_area(width, height):
    return width * height

def total_area():
    semicircle_rad = 4
    rectangle_wid = 5
    rectangle_hei = 8
    return semicircle_area(semicircle_rad) + rectangle_area(rectangle_wid, rectangle_hei)

if __name__ == '__main__':
    print(total_area())