def validate_vertices(vertices):
    if not all(isinstance(v, (int, float)) for v in vertices) or len(vertices) % 2 != 0:
        raise ValueError("Vertices must be a list of numbers with an even length")

def shoelace_area(vertices):
    validate_vertices(vertices)
    n = len(vertices) // 2
    area = 0.5 * abs(sum(vertices[i] * vertices[(i + 1) % n] - vertices[(i + 1) % n] * vertices[i] for i in range(n)))
    return area

if __name__ == '__main__':
    polygon1_vertices = [1, 2, 3, 4, 5, 6]
    polygon2_vertices = [2, 3, 4, 5, 6, 7]
    area1 = shoelace_area(polygon1_vertices)
    area2 = shoelace_area(polygon2_vertices)
    print(f"Area of the first shape: {area1}")
    print(f"Area of the second shape: {area2}")
    if area1 == area2:
        print("The areas of the two shapes are equal.")
    else:
        print("The areas of the two shapes are not equal.")