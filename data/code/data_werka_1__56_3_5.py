import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def compare_areas(rectangle_length, rectangle_width, circle_radius):
    rect_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    circ_area = calculate_circle_area(circle_radius)
    print(f'Rectangle Area: {rect_area:.2f}')
    print(f'Circle Area: {circ_area:.2f}')
if __name__ == '__main__':
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 4.0
    compare_areas(rectangle_length, rectangle_width, circle_radius)