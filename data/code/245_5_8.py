def shoelace_area(polygon):
    n = len(polygon)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0

def polygons_equal_area(poly1, poly2):
    return shoelace_area(poly1) == shoelace_area(poly2)
if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(polygons_equal_area(poly1, poly2))