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
def determine_larger_angle_sum(poly1_coords, poly2_coords):
    sum1 = calculate_angle_sum(poly1_coords)
    sum2 = calculate_angle_sum(poly2_coords)
    if sum1 > sum2:
        return "Polygon 1 has the larger total interior angle sum"
    elif sum2 > sum1:
        return "Polygon 2 has the larger total interior angle sum"
    else:
        return "Both polygons have the same total interior angle sum"
if __name__ == '__main__':
    triangle_coords = [
        (0, 0),
        (4, 0),
        (2, 3)
    ]
    quadrilateral_coords = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    result = determine_larger_angle_sum(triangle_coords, quadrilateral_coords)
    print(result)