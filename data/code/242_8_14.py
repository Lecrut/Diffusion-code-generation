from shapely.geometry import Polygon

def calculate_area(polygon):
    return polygon.area

if __name__ == '__main__':
    polygon1 = Polygon([(0,0), (3,0), (3,3), (0,3)])
    polygon2 = Polygon([(0,0), (5,0), (2,4)])
    area1 = calculate_area(polygon1)
    area2 = calculate_area(polygon2)
    print(f"Area of polygon 1: {area1}")
    print(f"Area of polygon 2: {area2}")
    if area1 > area2:
        print("Polygon 1 has a larger area.")
    elif area1 < area2:
        print("Polygon 2 has a larger area.")
    else:
        print("Both polygons have the same area.")