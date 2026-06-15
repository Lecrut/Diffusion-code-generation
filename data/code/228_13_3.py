def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    return [(x1, y1), (x2, y2), (x3, y3)]
if __name__ == '__main__':
    p1 = (0, 0)
    p2 = (3, 0)
    p3 = (0, 4)
    vertices = get_triangle_vertices(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
    print(vertices)