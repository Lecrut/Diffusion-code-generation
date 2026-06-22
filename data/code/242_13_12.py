def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

def compare_polygon_areas():
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    area1 = polygon_area(polygon1)
    area2 = polygon_area(polygon2)
    
    if area1 == area2:
        return "Areas are equal"
    else:
        return f"Area of first polygon: {area1}, Area of second polygon: {area2}"

if __name__ == '__main__':
    print(compare_polygon_areas())