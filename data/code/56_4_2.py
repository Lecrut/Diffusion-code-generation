import math
def calculate_angle_sum(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    angle_sum = 0.0
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n]
        v1 = math.sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)
        v2 = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
        v3 = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        try:
            angle = math.acos((v1**2 + v2**2 - v3**2) / (2 * v1 * v2))
            angle_sum += angle
        except ValueError:
            return float('inf')
    return angle_sum
def get_polygon_angle_sum(poly1, poly2):
    sum1 = calculate_angle_sum(poly1)
    sum2 = calculate_angle_sum(poly2)
    if sum1 > sum2:
        return "Polygon 1 has the larger total interior angle sum"
    elif sum2 > sum1:
        return "Polygon 2 has the larger total interior angle sum"
    else:
        return "Both polygons have the same total interior angle sum"
if __name__ == '__main__':
    triangle_vertices = [
        (0.0, 0.0),
        (4.0, 0.0),
        (0.0, 3.0)
    ]
    quadrilateral_vertices = [
        (0.0, 0.0),
        (4.0, 0.0),
        (4.0, 3.0),
        (0.0, 3.0)
    ]
    result = get_polygon_angle_sum(triangle_vertices, quadrilateral_vertices)
    print(result)