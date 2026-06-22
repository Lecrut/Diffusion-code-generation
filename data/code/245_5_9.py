def polygon_area(coords):
    n = len(coords)
    area = 0.5 * abs(sum(coords[i][0] * coords[(i + 1) % n][1] - coords[(i + 1) % n][0] * coords[i][1] for i in range(n)))
    return area

def polygons_equal_area(poly1, poly2):
    return polygon_area(poly1) == polygon_area(poly2)

if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(polygons_equal_area(poly1, poly2))