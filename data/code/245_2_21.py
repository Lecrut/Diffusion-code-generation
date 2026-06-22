def calculate_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def triangles_equal_area(t1, t2):
    return calculate_area(*t1) == calculate_area(*t2)

if __name__ == '__main__':
    triangle1 = ((-1, -1), (3, -1), (1, 3))
    triangle2 = ((2, 2), (6, 2), (4, 6))
    print(triangles_equal_area(triangle1, triangle2))