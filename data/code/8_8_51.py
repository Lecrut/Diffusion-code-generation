def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    area_calculator = {
        'x1': lambda i: vertices[i][0],
        'y1': lambda i: vertices[i][1],
        'x2': lambda i: vertices[(i + 1) % n][0],
        'y2': lambda i: vertices[(i + 1) % n][1]
    }
    
    total_area = 0.0
    for i in range(n):
        x1, y1, x2, y2 = (
            area_calculator['x1'](i),
            area_calculator['y1'](i),
            area_calculator['x2'](i),
            area_calculator['y2'](i)
        )
        total_area += (x1 * y2 - x2 * y1)
    
    return abs(total_area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_polygon_area(polygon_vertices))