import math

class Polygon:
    @staticmethod
    def calculate_angle_sum(vertices):
        n = len(vertices)
        if n < 3:
            return 0.0
        angle_sum = 0.0
        for i in range(n):
            a, b, c = vertices[i], vertices[(i + 1) % n], vertices[(i + 2) % n]
            v1 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
            v2 = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
            v3 = math.sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)
            if v1 == 0 or v2 == 0 or v3 == 0:
                continue
            try:
                cosine_angle = (v1**2 + v3**2 - v2**2) / (2 * v1 * v3)
                cosine_angle = max(-1.0, min(1.0, cosine_angle))
                angle_sum += math.acos(cosine_angle)
            except ValueError:
                return float('inf')
        return angle_sum

def compare_polygons(triangle_vertices, quadrilateral_vertices):
    triangle_angle_sum = Polygon.calculate_angle_sum(triangle_vertices)
    quadrilateral_angle_sum = Polygon.calculate_angle_sum(quadrilateral_vertices)
    if triangle_angle_sum > quadrilateral_angle_sum:
        return "Triangle has a larger total interior angle sum."
    elif quadrilateral_angle_sum > triangle_angle_sum:
        return "Quadrilateral has a larger total interior angle sum."
    else:
        return "Both polygons have the same total interior angle sum."

if __name__ == '__main__':
    triangle_vertices = [(0, 0), (1, 0), (0.5, math.sqrt(3)/2)]
    quadrilateral_vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
    
    result = compare_polygons(triangle_vertices, quadrilateral_vertices)
    print(result)