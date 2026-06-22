from shapely.geometry import Polygon

def calculate_polygon_area(points):
    return Polygon(points).area

if __name__ == '__main__':
    polygon1_points = [(0, 0), (3, 0), (3, 3), (0, 3)]
    polygon2_points = [(0, 0), (5, 0), (2, 4)]
    
    area1 = calculate_polygon_area(polygon1_points)
    area2 = calculate_polygon_area(polygon2_points)
    
    print(f"Area of polygon1: {area1}")
    print(f"Area of polygon2: {area2}")