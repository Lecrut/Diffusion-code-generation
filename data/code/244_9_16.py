def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

if __name__ == '__main__':
    POLYGON1 = [(0,0), (4,0), (4,3), (0,3)]
    POLYGON2 = [(1,1), (5,1), (5,4), (1,4)]
    total_area = polygon_area(POLYGON1) + polygon_area(POLYGON2)
    print(total_area)