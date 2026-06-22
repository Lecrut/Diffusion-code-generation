def shoelace_formula(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

def shapes_have_equal_area(shape1, shape2):
    if len(shape1) != len(shape2):
        raise ValueError("Both shapes must have the same number of vertices.")
    
    area_shape1 = shoelace_formula(shape1)
    area_shape2 = shoelace_formula(shape2)
    
    return area_shape1 == area_shape2

if __name__ == '__main__':
    shape1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    if shapes_have_equal_area(shape1, shape2):
        print("The areas of the two shapes are equal.")
    else:
        print("The areas of the two shapes are not equal.")