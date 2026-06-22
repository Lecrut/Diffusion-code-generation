import math

def calculate_angle_sum(vertices):
    if len(vertices) < 3:
        return 0.0
    
    def edge_length(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    def cosine_angle(p1, p2, p3):
        v1 = edge_length(p1, p3)
        v2 = edge_length(p2, p3)
        v3 = edge_length(p1, p2)
        
        if v1 == 0 or v2 == 0 or v3 == 0:
            return 0.0
        
        cos_angle = (v1**2 + v2**2 - v3**2) / (2 * v1 * v2)
        return max(-1.0, min(1.0, cos_angle))
    
    angle_sum = 0.0
    n = len(vertices)
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        p3 = vertices[(i + 2) % n]
        angle_sum += math.acos(cosine_angle(p1, p2, p3))
    
    return angle_sum

def larger_polygon_angle_sum(triangle, quadrilateral):
    triangle_angle_sum = calculate_angle_sum(triangle)
    quadrilateral_angle_sum = calculate_angle_sum(quadrilateral)
    
    if triangle_angle_sum > quadrilateral_angle_sum:
        return "Triangle"
    elif quadrilateral_angle_sum > triangle_angle_sum:
        return "Quadrilateral"
    else:
        return "Equal"

if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, math.sqrt(3)/2)]
    quadrilateral = [(0, 0), (1, 0), (1, 1), (0, 1)]
    
    result = larger_polygon_angle_sum(triangle, quadrilateral)
    print(result)