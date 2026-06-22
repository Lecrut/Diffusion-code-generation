def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("Polygon must have at least 3 vertices")
    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
        
    return abs(area) / 2.0

if __name__ == '__main__':
    poly = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = calculate_polygon_area(poly)
    print(result)