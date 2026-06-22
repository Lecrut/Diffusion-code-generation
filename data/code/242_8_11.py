def calculate_area(points):
    def polygon_area(points):
        n = len(points)
        area = 0.5 * abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n)))
        return area

    area1 = polygon_area([(0,0), (3,0), (3,3), (0,3)])
    area2 = polygon_area([(0,0), (5,0), (2,4)])
    
    print(f"Area of first polygon: {area1}")
    print(f"Area of second polygon: {area2}")
    if area1 > area2:
        print("First polygon has a larger area.")
    elif area1 < area2:
        print("Second polygon has a larger area.")
    else:
        print("Both polygons have the same area.")

if __name__ == '__main__':
    calculate_area([(0,0), (3,0), (3,3), (0,3)], [(0,0), (5,0), (2,4)])