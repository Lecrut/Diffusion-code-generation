def calculate_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def sum_areas(poly1, poly2):
    return calculate_area(poly1) + calculate_area(poly2)

if __name__ == '__main__':
    polygon1 = [(0,0), (4,0), (4,3), (0,3)]
    polygon2 = [(2,2), (6,2), (6,5), (2,5)]
    total_area = sum_areas(polygon1, polygon2)
    print(total_area)