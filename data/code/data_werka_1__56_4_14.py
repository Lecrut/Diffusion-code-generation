import math

def calculate_angle_sum(vertices):
    def edge_length(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def angle_between_edges(v1, v2):
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
        mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
        cosine_angle = dot_product / (mag_v1 * mag_v2)
        return math.acos(max(-1.0, min(1.0, cosine_angle)))

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
        
        angle = angle_between_edges(v1, v2)
        angle_sum += angle
    return angle_sum

def compare_polygon_angle_sums(triangle, quadrilateral):
    triangle_angle_sum = calculate_angle_sum(triangle)
    quadrilateral_angle_sum = calculate_angle_sum(quadrilateral)
    
    if triangle_angle_sum > quadrilateral_angle_sum:
        return "Triangle has a larger total interior angle sum."
    elif quadrilateral_angle_sum > triangle_angle_sum:
        return "Quadrilateral has a larger total interior angle sum."
    else:
        return "Both polygons have the same total interior angle sum."

if __name__ == '__main__':
    triangle = [(0, 0), (3, 0), (1.5, math.sqrt(6))]
    quadrilateral = [(0, 0), (4, 0), (4, 3), (0, 3)]
    
    result = compare_polygon_angle_sums(triangle, quadrilateral)
    print(result)