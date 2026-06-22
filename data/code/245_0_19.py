def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(x1*y2 - x2*y1 for (x1, y1), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1])))
    return area

if __name__ == '__main__':
    square_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    
    square_area = shoelace_area(square_vertices)
    triangle_area = shoelace_area(triangle_vertices)
    
    print(f"Square Area: {square_area}")
    print(f"Triangle Area: {triangle_area}")
    if square_area == triangle_area:
        print("The areas of the shapes are equal.")
    else:
        print("The areas of the shapes are not equal.")