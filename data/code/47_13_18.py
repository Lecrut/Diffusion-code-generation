def calculate_triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = abs(determinant) / 2.0
    return area
if __name__ == '__main__':
    vertex_a = (1, 1)
    vertex_b = (4, 5)
    vertex_c = (7, 2)
    area_result = calculate_triangle_area(vertex_a, vertex_b, vertex_c)
    print(f'The area of the triangle is: {area_result}')