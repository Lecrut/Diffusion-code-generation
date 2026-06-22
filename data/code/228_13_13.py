def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    vertices = get_triangle_vertices(0, 0, 3, 0, 1, 4)
    print(vertices)