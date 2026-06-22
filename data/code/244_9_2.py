def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

if __name__ == '__main__':
    polygon1 = [(0,0), (4,0), (4,3), (0,3)]
    polygon2 = [(1,1), (5,1), (5,4), (1,4)]
    print(polygon_area(polygon1) + polygon_area(polygon2))