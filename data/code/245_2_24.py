def calculate_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def validate_triangle(triangle):
    if len(triangle) != 3:
        raise ValueError("Triangle must have exactly three points")
    for point in triangle:
        if len(point) != 2:
            raise ValueError("Each point must be a tuple of two coordinates")

def triangles_equal_area(t1, t2):
    validate_triangle(t1)
    validate_triangle(t2)
    return calculate_area(*t1) == calculate_area(*t2)

if __name__ == '__main__':
    triangle1 = ((0, 0), (4, 0), (2, 3))
    triangle2 = ((-2, -3), (2, -3), (0, 0))
    print(triangles_equal_area(triangle1, triangle2))