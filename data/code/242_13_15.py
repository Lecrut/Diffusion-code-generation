def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum((vertices[i][0] * vertices[(i + 1) % n][1] - vertices[i][1] * vertices[(i + 1) % n][0]) for i in range(n)))
    return area

def compare_areas(poly1, poly2):
    area_poly1 = shoelace_area(poly1)
    area_poly2 = shoelace_area(poly2)
    
    if area_poly1 == area_poly2:
        return "Areas are equal."
    elif area_poly1 < area_poly2:
        return f"Polygon 1 has a smaller area by {abs(area_poly1 - area_poly2)}."
    else:
        return f"Polygon 1 has a larger area by {abs(area_poly1 - area_poly2)}."

if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    result = compare_areas(polygon1, polygon2)
    print(result)