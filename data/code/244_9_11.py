def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("Polygon must have at least 3 vertices")
    
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def sum_areas(poly1, poly2):
    return polygon_area(poly1) + polygon_area(poly2)

if __name__ == '__main__':
    poly1 = [(0,0), (4,0), (4,3), (0,3)]
    poly2 = [(1,1), (5,1), (5,4), (1,4)]
    
    if len(poly1) < 3 or len(poly2) < 3:
        print("One of the polygons has fewer than 3 vertices")
    else:
        total_area = sum_areas(poly1, poly2)
        print(total_area)