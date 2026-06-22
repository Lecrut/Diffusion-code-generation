def shoelace_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

def compare_areas(polygon1, polygon2):
    area1 = shoelace_area(polygon1)
    area2 = shoelace_area(polygon2)
    if area1 == area2:
        return "Areas are equal"
    elif area1 > area2:
        return f"Area of polygon 1 is larger by {area1 - area2:.2f}"
    else:
        return f"Area of polygon 2 is larger by {area2 - area1:.2f}"

if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    result = compare_areas(polygon1, polygon2)
    print(result)