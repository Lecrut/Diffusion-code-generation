import math

def scaled_area_rectangle(length, width, scale):
    return length * width * scale

def scaled_area_circle(radius, scale):
    return math.pi * radius ** 2 * scale
if __name__ == '__main__':
    rect_length = 5.0
    rect_width = 3.0
    rect_scale = 2.0
    circle_radius = 4.0
    circle_scale = 1.5
    rectangle_area = scaled_area_rectangle(rect_length, rect_width, rect_scale)
    circle_area = scaled_area_circle(circle_radius, circle_scale)
    print(f'Scaled area of the rectangle: {rectangle_area}')
    print(f'Scaled area of the circle: {circle_area}')