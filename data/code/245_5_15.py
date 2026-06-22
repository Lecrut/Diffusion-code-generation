def shoelace_area(coords):
    area = 0
    n = len(coords)
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def are_areas_equal(polygon1, polygon2):
    area1 = shoelace_area(polygon1)
    area2 = shoelace_area(polygon2)
    return area1 == area2
if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(2, 0), (6, 0), (6, 3), (2, 3)]
    print(are_areas_equal(poly1, poly2))