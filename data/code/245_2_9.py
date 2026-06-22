def triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def triangles_equal_area(t1, t2):
    return triangle_area(*t1) == triangle_area(*t2)

if __name__ == '__main__':
    triangle1 = ((0, 0), (4, 0), (2, 3))
    triangle2 = ((-2, -3), (2, -3), (0, 0))
    print(triangles_equal_area(triangle1, triangle2))