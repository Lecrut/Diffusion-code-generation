def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x1*y2 - x2*y1 for (x1, y1), (x2, y2) in zip(vertices, vertices[1:] + [vertices[0]])))
    return area

def validate_vertices(vertices):
    if not all(isinstance(v, tuple) and len(v) == 2 for v in vertices):
        raise ValueError("Vertices must be a list of tuples representing 2D points.")
    if len(vertices) < 3:
        raise ValueError("There must be at least three vertices to form a polygon.")

def shapes_have_equal_area(shape1_vertices, shape2_vertices):
    validate_vertices(shape1_vertices)
    validate_vertices(shape2_vertices)
    return shoelace_area(shape1_vertices) == shoelace_area(shape2_vertices)

if __name__ == '__main__':
    rectangle = [(0, 0), (4, 0), (4, 3), (0, 3)]
    triangle = [(0, 0), (4, 0), (2, 3)]
    
    if shapes_have_equal_area(rectangle, triangle):
        print("The areas of the rectangle and the triangle are equal.")
    else:
        print("The areas of the rectangle and the triangle are not equal.")