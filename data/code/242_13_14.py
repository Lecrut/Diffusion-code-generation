def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

def compare_polygon_areas():
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    area1 = polygon_area(poly1)
    area2 = polygon_area(poly2)
    
    if area1 == area2:
        return "The areas of the two polygons are equal."
    else:
        return f"The areas of the two polygons are not equal. Area 1: {area1}, Area 2: {area2}"

if __name__ == '__main__':
    print(compare_polygon_areas())