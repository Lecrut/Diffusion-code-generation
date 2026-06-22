import math
POLYGON1_VERTICES = [(0, 0), (3, 0), (3, 3), (0, 3)]
POLYGON2_VERTICES = [(0, 0), (5, 0), (2, 4)]

def calculate_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum([vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)]))
    return area

def compare_areas(area1, area2):
    if area1 > area2:
        return 'Polygon 1 is larger'
    elif area1 < area2:
        return 'Polygon 2 is larger'
    else:
        return 'Both polygons have the same area'
if __name__ == '__main__':
    area1 = calculate_area(POLYGON1_VERTICES)
    area2 = calculate_area(POLYGON2_VERTICES)
    comparison_result = compare_areas(area1, area2)
    print(f'Area of Polygon 1: {area1}')
    print(f'Area of Polygon 2: {area2}')
    print(comparison_result)