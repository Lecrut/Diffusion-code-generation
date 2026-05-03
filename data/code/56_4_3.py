import math
def calculate_angle_sum(vertices):
    sum_angles = 0
    n = len(vertices)
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        p3 = vertices[(i + 2) % n]
        v1 = (p1[0], p1[1])
        v2 = (p2[0], p2[1])
        v3 = (p3[0], p3[1])
        v12_x = v2[0] - v1[0]
        v12_y = v2[1] - v1[1]
        v13_x = v3[0] - v1[0]
        v13_y = v3[1] - v1[1]
        dot_product = v12_x * v13_x + v12_y * v13_y
        mag12 = math.sqrt(v12_x**2 + v12_y**2)
        mag13 = math.sqrt(v13_x**2 + v13_y**2)
        if mag12 == 0 or mag13 == 0:
            continue
        cosine_angle = dot_product / (mag12 * mag13)
        cosine_angle = max(-1.0, min(1.0, cosine_angle))
        angle = math.acos(cosine_angle)
        sum_angles += angle
    return sum_angles
def solve():
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
    triangle_sum = calculate_angle_sum(triangle_vertices)
    quadrilateral_sum = calculate_angle_sum(quadrilateral_vertices)
    if triangle_sum > quadrilateral_sum:
        result = "Triangle has the larger total interior angle sum"
    elif quadrilateral_sum > triangle_sum:
        result = "Quadrilateral has the larger total interior angle sum"
    else:
        result = "Both polygons have the same total interior angle sum"
    print(result)
if __name__ == '__main__':
    solve()