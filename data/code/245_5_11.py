def shoelace_area(coords):
    n = len(coords)
    area = 0.5 * abs(sum((coords[i][0] * coords[(i + 1) % n][1] - coords[(i + 1) % n][0] * coords[i][1] for i in range(n))))
    return area

def are_areas_equal(polygon1, polygon2):
    return shoelace_area(polygon1) == shoelace_area(polygon2)
if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(5, 5), (9, 5), (9, 8), (5, 8)]
    print(are_areas_equal(poly1, poly2))