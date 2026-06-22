def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def compare_polygon_areas():
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    area1 = polygon_area(polygon1)
    area2 = polygon_area(polygon2)
    
    if area1 == area2:
        return "The polygons have equal areas."
    else:
        return "The polygons do not have equal areas."

if __name__ == '__main__':
    print(compare_polygon_areas())