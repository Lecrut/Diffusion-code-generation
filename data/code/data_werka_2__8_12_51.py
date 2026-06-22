import math

def scaled_area_rectangle(width, height, scale_factor):
    return width * height * scale_factor

def scaled_area_circle(radius, scale_factor):
    return math.pi * (radius ** 2) * scale_factor

if __name__ == '__main__':
    rectangle_width = 5.0
    rectangle_height = 10.0
    circle_radius = 7.0
    scale_factor = 2.5
    
    rectangle_scaled_area = scaled_area_rectangle(rectangle_width, rectangle_height, scale_factor)
    circle_scaled_area = scaled_area_circle(circle_radius, scale_factor)
    
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')