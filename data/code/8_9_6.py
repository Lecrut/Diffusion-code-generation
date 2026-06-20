def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle = [(0, 0), (3, 0), (0, 4)]
    pentagon = [(1, 0), (2, 1), (2, 3), (0, 4), (-1, 1)]
    
    square_area = calculate_polygon_area(square)
    triangle_area = calculate_polygon_area(triangle)
    pentagon_area = calculate_polygon_area(pentagon)
    
    print(square_area)
    print(triangle_area)
    print(pentagon_area)