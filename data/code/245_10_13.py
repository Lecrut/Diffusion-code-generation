import math

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def shapes_equal_area(circle_radius, rect_length, rect_width):
    return circle_area(circle_radius) == rectangle_area(rect_length, rect_width)

if __name__ == '__main__':
    print(shapes_equal_area(3, 6, 3))