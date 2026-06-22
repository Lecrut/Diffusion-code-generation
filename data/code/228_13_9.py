def get_triangle_vertices(x1, y1, x2, y2, x3, y3):
    if not (isinstance(x1, (int, float)) and isinstance(y1, (int, float))
            and isinstance(x2, (int, float)) and isinstance(y2, (int, float))
            and isinstance(x3, (int, float)) and isinstance(y3, (int, float))):
        raise ValueError("All coordinates must be numbers.")
    
    return [(x1, y1), (x2, y2), (x3, y3)]

if __name__ == '__main__':
    x1_val = 0
    y1_val = 0
    x2_val = 3
    y2_val = 0
    x3_val = 1.5
    y3_val = 4
    vertices = get_triangle_vertices(x1_val, y1_val, x2_val, y2_val, x3_val, y3_val)
    print(vertices)