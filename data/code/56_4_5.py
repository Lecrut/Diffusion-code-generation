import math
def calculate_angle_sum(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    angle_sum = 0.0
    for i in range(n):
        a1 = vertices[(i - 1 + n) % n]
        a2 = vertices[i]
        a3 = vertices[(i + 1) % n]
        v1 = math.hypot(a1[0] - a2[0], a1[1] - a2[1])
        v2 = math.hypot(a3[0] - a2[0], a3[1] - a2[1])
        dot_product = (a1[0] - a2[0]) * (a3[0] - a2[0]) + (a1[1] - a2[1]) * (a3[1] - a2[1])
        cosine_angle = dot_product / (v1 * v2)
        cosine_angle = max(-1.0, min(1.0, cosine_angle))
        angle = math.acos(cosine_angle)
        angle_sum += angle
    return angle_sum
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
        (0.0, 0.0),
        (4.0, 0.0),
        (0.0, 3.0)
    ]
    quadrilateral_coords = [
        (0.0, 0.0),
        (4.0, 0.0),
        (4.0, 3.0),
        (0.0, 3.0)
    ]
    result = determine_larger_angle_sum(triangle_coords, quadrilateral_coords)
    print(result)