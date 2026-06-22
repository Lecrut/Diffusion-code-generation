def shoelace_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    shape1_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2_vertices = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    area1 = shoelace_area(shape1_vertices)
    area2 = shoelace_area(shape2_vertices)
    
    if area1 == area2:
        print("The areas of the two shapes are equal.")
    else:
        print("The areas of the two shapes are not equal.")