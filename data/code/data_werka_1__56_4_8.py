import math

def calculate_angle_sum(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    angle_sum = 0.0
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n]
        v1x, v1y = b[0] - a[0], b[1] - a[1]
        v2x, v2y = c[0] - b[0], c[1] - b[1]
        dot_product = v1x * v2x + v1y * v2y
        mag_v1 = math.sqrt(v1x**2 + v1y**2)
        mag_v2 = math.sqrt(v2x**2 + v2y**2)
        if mag_v1 == 0 or mag_v2 == 0:
            continue
        cos_angle = dot_product / (mag_v1 * mag_v2)
        angle = math.acos(max(-1.0, min(1.0, cos_angle)))
        angle_sum += angle
    return angle_sum

def compare_polygons(triangle_vertices, quadrilateral_vertices):
    triangle_angle_sum = calculate_angle_sum(triangle_vertices)
    quadrilateral_angle_sum = calculate_angle_sum(quadrilateral_vertices)
    if triangle_angle_sum > quadrilateral_angle_sum:
        return "Triangle"
    elif quadrilateral_angle_sum > triangle_angle_sum:
        return "Quadrilateral"
    else:
        return "Equal"

if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, math.sqrt(3)/2)]
    quadrilateral = [(0, 0), (1, 0), (1, 1), (0, 1)]
    
    result = compare_polygons(triangle, quadrilateral)
    print(result)