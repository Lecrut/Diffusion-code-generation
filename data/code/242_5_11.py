import math

GEOMETRY_PARAMS = {
    'ellipse': {'a': 5, 'b': 3},
    'triangle': {'base': 10, 'height': 4}
}

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(GEOMETRY_PARAMS['ellipse']['a'], GEOMETRY_PARAMS['ellipse']['b'])
    triangle_area = calculate_area_triangle(GEOMETRY_PARAMS['triangle']['base'], GEOMETRY_PARAMS['triangle']['height'])
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")