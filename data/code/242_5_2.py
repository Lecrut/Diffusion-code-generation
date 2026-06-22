import math

def calculate_area(ellipse_params, triangle_params):
    semi_major_axis, semi_minor_axis = ellipse_params
    base, height = triangle_params
    
    ellipse_area = math.pi * semi_major_axis * semi_minor_axis
    triangle_area = 0.5 * base * height
    
    return ellipse_area, triangle_area

if __name__ == '__main__':
    params = {
        'ellipse': (5, 3),
        'triangle': (10, 4)
    }
    
    ellipse_area, triangle_area = calculate_area(params['ellipse'], params['triangle'])
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")