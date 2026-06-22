def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def sum_areas(area1, area2):
    return area1 + area2

if __name__ == '__main__':
    polygon1 = [(0,0), (4,0), (4,3), (0,3)]
    polygon2 = [(1,1), (5,1), (5,4), (1,4)]
    
    area1 = polygon_area(polygon1)
    area2 = polygon_area(polygon2)
    
    total_area = sum_areas(area1, area2)
    print(total_area)