import numpy as np

def shoelace_formula(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x*y - y*x for x, y in zip(vertices, vertices[1:] + vertices[:1])))
    return area

def shapes_equal_area(vertices1, vertices2):
    return np.isclose(shoelace_formula(vertices1), shoelace_formula(vertices2))

if __name__ == '__main__':
    shape1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    if shapes_equal_area(shape1, shape2):
        print("The areas of the two shapes are equal.")
    else:
        print("The areas of the two shapes are not equal.")