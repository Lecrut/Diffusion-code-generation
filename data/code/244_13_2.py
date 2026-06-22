import math

def ellipse_area(a, b):
    return math.pi * a * b

def combined_ellipse_areas(axes_dict):
    area1 = ellipse_area(axes_dict['ellipse1']['a'], axes_dict['ellipse1']['b'])
    area2 = ellipse_area(axes_dict['ellipse2']['a'], axes_dict['ellipse2']['b'])
    return area1 + area2

if __name__ == '__main__':
    ellipses = {
        'ellipse1': {'a': 3, 'b': 4},
        'ellipse2': {'a': 5, 'b': 6}
    }
    total_area = combined_ellipse_areas(ellipses)
    print(total_area)