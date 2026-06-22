import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    semi_major_axis = 6
    semi_minor_axis = 2
    base = 12
    height = 3
    
    ellipse_area = calculate_area_ellipse(semi_major_axis, semi_minor_axis)
    triangle_area = calculate_area_triangle(base, height)
    
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")