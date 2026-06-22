import math

def calculate_area_ellipse(a, b):
    return math.pi * a * b

def calculate_area_triangle(b, h):
    return 0.5 * b * h

if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(5, 3)
    triangle_area = calculate_area_triangle(10, 4)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")