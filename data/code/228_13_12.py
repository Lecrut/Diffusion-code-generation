def validate_points(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3]):
        raise ValueError("All coordinates must be numbers")
    return True

def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    validate_points(x1, y1, x2, y2, x3, y3)
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    try:
        x1_val = 0
        y1_val = 0
        x2_val = 3
        y2_val = 0
        x3_val = 1.5
        y3_val = 4
        vertices = get_triangle_vertices(x1_val, y1_val, x2_val, y2_val, x3_val, y3_val)
        print(vertices)
    except ValueError as e:
        print(e)