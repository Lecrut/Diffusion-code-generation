def generate_rectangle_vertices(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
if __name__ == '__main__':
    x_min = 0
    y_min = 0
    x_max = 4
    y_max = 3
    vertices = [
        (x_min, y_min),
        (x_max, y_min),
        (x_max, y_max),
        (x_min, y_max)
    ]
    print(vertices)