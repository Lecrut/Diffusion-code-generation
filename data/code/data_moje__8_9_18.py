def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
        
    area = abs(area) / 2.0
    
    if isinstance(area, float):
        if area == 0.0:
            return 0.0
        if abs(area) < 1e-10:
            return 0.0
            
    return round(area, 10)

if __name__ == '__main__':
    sample_polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = calculate_polygon_area(sample_polygon)
    print(result)