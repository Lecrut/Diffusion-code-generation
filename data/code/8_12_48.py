import math

def calculate_rectangle_scaled_area(width, height, scale_factor):
    area = width * height
    return area * scale_factor

def calculate_circle_scaled_area(radius, scale_factor):
    area = math.pi * (radius ** 2)
    return area * scale_factor

if __name__ == '__main__':
    rectangle_width = 5.0
    rectangle_height = 10.0
    circle_radius = 7.0
    scale_factor = 2.5
    
    rectangle_scaled_area = calculate_rectangle_scaled_area(rectangle_width, rectangle_height, scale_factor)
    circle_scaled_area = calculate_circle_scaled_area(circle_radius, scale_factor)
    
    print(f"Scaled area of the rectangle: {rectangle_scaled_area}")
    print(f"Scaled area of the circle: {circle_scaled_area}")