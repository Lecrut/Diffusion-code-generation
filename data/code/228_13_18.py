def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    x1_val = 0
    y1_val = 0
    x2_val = 4
    y2_val = 0
    x3_val = 2
    y3_val = 3
    vertices = get_triangle_vertices(x1_val, y1_val, x2_val, y2_val, x3_val, y3_val)
    print(vertices)