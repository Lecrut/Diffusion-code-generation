from shapely.geometry import Polygon

def calculate_area(poly):
    return poly.area

def compare_areas(poly1, poly2):
    area1 = calculate_area(poly1)
    area2 = calculate_area(poly2)
    if area1 > area2:
        return f"Polygon 1 has a larger area: {area1}"
    elif area1 < area2:
        return f"Polygon 2 has a larger area: {area2}"
    else:
        return "Both polygons have the same area"

if __name__ == '__main__':
    poly1 = Polygon([(0,0), (3,0), (3,3), (0,3)])
    poly2 = Polygon([(0,0), (5,0), (2,4)])
    result = compare_areas(poly1, poly2)
    print(result)