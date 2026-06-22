def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x*y - y*x for x, y in zip(vertices, vertices[1:] + vertices[:1])))
    return area

if __name__ == '__main__':
    poly1 = [(0,0), (4,0), (4,3), (0,3)]
    poly2 = [(1,1), (5,1), (5,4), (1,4)]
    print(polygon_area(poly1) + polygon_area(poly2))