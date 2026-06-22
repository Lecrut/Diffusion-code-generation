import math

def area_of_ellipse(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    ellipse_areas = {
        'ellipse1': {'a': 3, 'b': 2},
        'ellipse2': {'a': 4, 'b': 1}
    }
    total_area = area_of_ellipse(ellipse_areas['ellipse1']['a'], ellipse_areas['ellipse1']['b']) + \
                 area_of_ellipse(ellipse_areas['ellipse2']['a'], ellipse_areas['ellipse2']['b'])
    print(total_area)