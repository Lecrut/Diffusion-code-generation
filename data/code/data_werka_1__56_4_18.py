import math

def calculate_angle_sum(vertices):
    def edge_length(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def angle_between_edges(v1, v2, v3):
        a = edge_length(v1, v2)
        b = edge_length(v2, v3)
        c = edge_length(v3, v1)
        try:
            cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
            cos_angle = max(-1.0, min(1.0, cos_angle))
            return math.acos(cos_angle)
        except ValueError:
            return float('inf')

    n = len(vertices)
    if n < 3:
        return 0.0

    angle_sum = 0.0
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        v3 = vertices[(i + 2) % n]
        angle_sum += angle_between_edges(v1, v2, v3)

    return angle_sum

def compare_polygons(triangle_vertices, quadrilateral_vertices):
    triangle_angle_sum = calculate_angle_sum(triangle_vertices)
    quadrilateral_angle_sum = calculate_angle_sum(quadrilateral_vertices)

    if triangle_angle_sum > quadrilateral_angle_sum:
        return "Triangle has a larger total interior angle sum."
    elif triangle_angle_sum < quadrilateral_angle_sum:
        return "Quadrilateral has a larger total interior angle sum."
    else:
        return "Both polygons have the same total interior angle sum."

if __name__ == '__main__':
    triangle = [(0, 0), (3, 0), (1.5, math.sqrt(27))]
    quadrilateral = [(0, 0), (4, 0), (4, 3), (0, 3)]

    result = compare_polygons(triangle, quadrilateral)
    print(result)