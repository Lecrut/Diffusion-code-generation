import math

def ellipse_area(a, b):
    return math.pi * a * b

def combined_ellipse_areas(axes1, axes2):
    area1 = ellipse_area(axes1['a'], axes1['b'])
    area2 = ellipse_area(axes2['a'], axes2['b'])
    return area1 + area2

if __name__ == '__main__':
    ellipses = {
        'ellipse1': {'a': 7, 'b': 8},
        'ellipse2': {'a': 9, 'b': 10}
    }
    total_area = combined_ellipse_areas(ellipses['ellipse1'], ellipses['ellipse2'])
    print(total_area)