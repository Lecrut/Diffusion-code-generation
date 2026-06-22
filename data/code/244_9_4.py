def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

if __name__ == '__main__':
    polygon1_vertices = [(0,0), (4,0), (4,3), (0,3)]
    polygon2_vertices = [(2,2), (6,2), (6,5), (2,5)]
    
    area_polygon1 = calculate_polygon_area(polygon1_vertices)
    area_polygon2 = calculate_polygon_area(polygon2_vertices)
    
    total_area = area_polygon1 + area_polygon2
    print(total_area)