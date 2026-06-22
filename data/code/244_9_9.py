def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

def sum_of_areas(poly1, poly2):
    return polygon_area(poly1) + polygon_area(poly2)

if __name__ == '__main__':
    poly1 = [(0,0), (4,0), (4,3), (0,3)]
    poly2 = [(1,1), (5,1), (5,4), (1,4)]
    print(sum_of_areas(poly1, poly2))