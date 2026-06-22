import math

class Shape:
    def __init__(self, vertices):
        self.vertices = vertices

    def area(self):
        n = len(self.vertices)
        area = 0.5 * abs(sum(self.vertices[i][0] * self.vertices[(i + 1) % n][1]
                              - self.vertices[i][1] * self.vertices[(i + 1) % n][0]
                              for i in range(n)))
        return area

def shapes_have_equal_area(shape1, shape2):
    return math.isclose(shape1.area(), shape2.area())

if __name__ == '__main__':
    vertices_triangle = [(0, 0), (4, 0), (2, 3)]
    vertices_square = [(0, 0), (4, 0), (4, 4), (0, 4)]

    triangle = Shape(vertices_triangle)
    square = Shape(vertices_square)

    print("Triangle area:", triangle.area())
    print("Square area:", square.area())

    if shapes_have_equal_area(triangle, square):
        print("The areas of the triangle and the square are equal.")
    else:
        print("The areas of the triangle and the square are not equal.")