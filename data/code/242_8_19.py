def calculate_area(points):
    if len(points) < 3:
        raise ValueError("Polygon must have at least 3 points")
    
    area = 0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def compare_areas(polygon1, polygon2):
    area1 = calculate_area(polygon1)
    area2 = calculate_area(polygon2)
    print(f"Polygon 1 Area: {area1}")
    print(f"Polygon 2 Area: {area2}")
    if area1 > area2:
        print("Polygon 1 has a larger area.")
    elif area1 < area2:
        print("Polygon 2 has a larger area.")
    else:
        print("Both polygons have the same area.")

if __name__ == '__main__':
    polygon1 = [(0,0), (3,0), (3,3), (0,3)]
    polygon2 = [(0,0), (5,0), (2,4)]
    compare_areas(polygon1, polygon2)