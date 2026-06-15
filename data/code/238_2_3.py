def generate_rectangle_vertices(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
if __name__ == '__main__':
    x_min = 1
    y_min = 5
    x_max = 10
    y_max = 8
    vertices = [(x, y) for x in [x_min, x_max] for y in [y_min, y_max]]
    print(vertices)