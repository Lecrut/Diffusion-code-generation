def calculate_polygon_area(points):
    n = len(points)
    area = 0.5 * abs(sum(x1*y2 - x2*y1 for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])))
    return area

if __name__ == '__main__':
    polygon1_points = [(0,0), (3,0), (3,3), (0,3)]
    polygon2_points = [(0,0), (5,0), (2,4)]

    area1 = calculate_polygon_area(polygon1_points)
    area2 = calculate_polygon_area(polygon2_points)

    print(f"Polygon 1 Area: {area1}")
    print(f"Polygon 2 Area: {area2}")