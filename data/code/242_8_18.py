from shapely.geometry import Polygon

def calculate_area_and_compare(polygon1, polygon2):
    area1 = polygon1.area
    area2 = polygon2.area
    return area1, area2, area1 > area2

if __name__ == '__main__':
    poly1 = Polygon([(0,0), (3,0), (3,3), (0,3)])
    poly2 = Polygon([(0,0), (5,0), (2,4)])
    area1, area2, is_larger = calculate_area_and_compare(poly1, poly2)
    print(f"Area of first polygon: {area1}")
    print(f"Area of second polygon: {area2}")
    print(f"Is the first polygon larger? {'Yes' if is_larger else 'No'}")