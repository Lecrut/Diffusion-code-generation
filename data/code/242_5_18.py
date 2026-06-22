import math

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    areas = {
        'ellipse': (5, 3),
        'triangle': (10, 4)
    }
    ellipse_area = calculate_area_ellipse(*areas['ellipse'])
    triangle_area = calculate_area_triangle(*areas['triangle'])
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")