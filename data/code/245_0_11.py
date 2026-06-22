def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

if __name__ == '__main__':
    shape1_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2_vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
    
    area1 = shoelace_area(shape1_vertices)
    area2 = shoelace_area(shape2_vertices)
    
    if area1 == area2:
        print("The areas of the two shapes are equal.")
    else:
        print(f"Area of shape 1: {area1}")
        print(f"Area of shape 2: {area2}")