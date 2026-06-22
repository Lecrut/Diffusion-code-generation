import math

def calculate_area(figure_type, params):
    if figure_type == 'ellipse':
        semi_major_axis, semi_minor_axis = params
        return math.pi * semi_major_axis * semi_minor_axis
    elif figure_type == 'triangle':
        base, height = params
        return 0.5 * base * height

if __name__ == '__main__':
    figures = {
        'ellipse': (5, 3),
        'triangle': (10, 4)
    }
    ellipse_area = calculate_area('ellipse', figures['ellipse'])
    triangle_area = calculate_area('triangle', figures['triangle'])
    print(f"Ellipse area: {ellipse_area}")
    print(f"Triangle area: {triangle_area}")