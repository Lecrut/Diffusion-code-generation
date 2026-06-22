def calculate_area_difference(polygon1_vertices, polygon2_vertices):
    def shoelace_formula(vertices):
        n = len(vertices)
        area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
        return area

    area_polygon1 = shoelace_formula(polygon1_vertices)
    area_polygon2 = shoelace_formula(polygon2_vertices)

    if area_polygon1 == area_polygon2:
        result = "Areas are equal"
    else:
        result = f"Area of polygon 1 is {area_polygon1}, Area of polygon 2 is {area_polygon2}"

    return result

if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3)]
    polygon2 = [(0, 0), (5, 0), (5, 4), (0, 4)]
    comparison_result = calculate_area_difference(polygon1, polygon2)
    print(comparison_result)