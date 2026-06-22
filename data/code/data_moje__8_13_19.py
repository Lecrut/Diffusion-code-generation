import math

def calculate_scaled_rectangle_area(width, height, scale):
    if scale <= 0:
        raise ValueError("Scale factor must be positive")
    scaled_width = width * scale
    scaled_height = height * scale
    return scaled_width * scaled_height

def calculate_scaled_circle_area(radius, scale):
    if scale <= 0:
        raise ValueError("Scale factor must be positive")
    scaled_radius = radius * scale
    return math.pi * (scaled_radius ** 2)

if __name__ == '__main__':
    rect_w = 10
    rect_h = 5
    rect_scale = 2
    circle_r = 3
    circle_scale = 1.5

    rect_area = calculate_scaled_rectangle_area(rect_w, rect_h, rect_scale)
    circle_area = calculate_scaled_circle_area(circle_r, circle_scale)

    print(rect_area)
    print(circle_area)