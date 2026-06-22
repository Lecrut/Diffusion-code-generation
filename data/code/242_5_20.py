import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    ellipse_params = (7, 4)
    triangle_params = (12, 6)
    
    ellipse_area = calculate_area_ellipse(*ellipse_params)
    triangle_area = calculate_area_triangle(*triangle_params)
    
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")