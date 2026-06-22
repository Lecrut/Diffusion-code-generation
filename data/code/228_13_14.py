def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3]):
        raise ValueError("All coordinates must be integers or floats.")
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    try:
        vertices = get_triangle_vertices(0, 0, 3, 0, 1.5, 4)
        print(vertices)
    except ValueError as e:
        print(e)