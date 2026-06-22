def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def compare_polygons(poly1, poly2):
    area1 = polygon_area(poly1)
    area2 = polygon_area(poly2)
    if area1 == area2:
        return "The polygons have equal areas."
    else:
        return "The polygons do not have equal areas."

if __name__ == '__main__':
    sample_poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    sample_poly2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(compare_polygons(sample_poly1, sample_poly2))