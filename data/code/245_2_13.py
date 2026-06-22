def calculate_triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def are_areas_equal(triangle1, triangle2):
    return calculate_triangle_area(*triangle1) == calculate_triangle_area(*triangle2)

if __name__ == '__main__':
    triangle_a = ((0, 0), (4, 0), (2, 3))
    triangle_b = ((-2, -3), (2, -3), (0, 0))
    print(are_areas_equal(triangle_a, triangle_b))