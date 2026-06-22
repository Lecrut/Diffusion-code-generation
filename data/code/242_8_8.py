from shapely.geometry import Polygon

def calculate_and_compare_areas():
    polygon1 = Polygon([(0,0), (3,0), (3,3), (0,3)])
    polygon2 = Polygon([(0,0), (5,0), (2,4)])
    
    area1 = polygon1.area
    area2 = polygon2.area
    
    print(f"Area of first polygon: {area1}")
    print(f"Area of second polygon: {area2}")
    
    if area1 > area2:
        print("First polygon has a larger area.")
    elif area1 < area2:
        print("Second polygon has a larger area.")
    else:
        print("Both polygons have the same area.")

if __name__ == '__main__':
    calculate_and_compare_areas()