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
        vec_a = (v1[0] - v3[0], v1[1] - v3[1])
        vec_b = (v2[0] - v3[0], v2[1] - v3[1])
        dot_product = vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]
        mag_a = math.sqrt(vec_a[0]**2 + vec_a[1]**2)
        mag_b = math.sqrt(vec_b[0]**2 + vec_b[1]**2)
        if mag_a == 0 or mag_b == 0:
            continue
        cosine_angle = dot_product / (mag_a * mag_b)
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
        result = "Triangle"
    elif quadrilateral_sum > triangle_sum:
        result = "Quadrilateral"
    else:
        result = "Equal"
    print(result)
if __name__ == '__main__':
    solve()