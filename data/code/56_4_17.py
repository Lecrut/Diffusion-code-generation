import math
PI = math.pi

def calculate_angle_sum(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    angle_sum = 0.0
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n]
        v1 = (b[0] - a[0], b[1] - a[1])
        v2 = (c[0] - b[0], c[1] - b[1])
        v3 = (c[0] - a[0], c[1] - a[1])
        mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
        mag_v3 = math.sqrt(v3[0] ** 2 + v3[1] ** 2)
        if mag_v1 == 0 or mag_v2 == 0 or mag_v3 == 0:
            continue
        try:
            cos_angle = (v1[0] * v3[0] + v1[1] * v3[1]) / (mag_v1 * mag_v3)
            cos_angle = max(-1.0, min(1.0, cos_angle))
            angle = math.acos(cos_angle)
            angle_sum += angle
        except ValueError:
            return float('inf')
    return angle_sum

def compare_polygons(triangle_vertices, quadrilateral_vertices):
    triangle_angle_sum = calculate_angle_sum(triangle_vertices)
    quadrilateral_angle_sum = calculate_angle_sum(quadrilateral_vertices)
    if triangle_angle_sum > quadrilateral_angle_sum:
        return 'Triangle'
    else:
        return 'Quadrilateral'
if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)]
    quadrilateral = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = compare_polygons(triangle, quadrilateral)
    print(result)