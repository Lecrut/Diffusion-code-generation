import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(width, height):
    return width * height

def sum_areas(circle_radius, rectangle_width, rectangle_height):
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_width, rectangle_height)
    return circle_area + rectangle_area

if __name__ == '__main__':
    print(sum_areas(3, 4, 5))