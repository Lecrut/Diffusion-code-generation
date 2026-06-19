def calculate_angle_sum(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    
    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]
    
    def magnitude(v):
        return (v[0]**2 + v[1]**2)**0.5
    
    angle_sum = 0.0
    for i in range(n):
        a = vertices[i]
        b = vertices[(i + 1) % n]
        c = vertices[(i + 2) % n]
        
        v1 = (b[0] - a[0], b[1] - a[1])
        v2 = (c[0] - b[0], c[1] - b[1])
        
        cos_angle = dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_sum += math.acos(cos_angle)
    
    return angle_sum

def compare_polygons(polygon1, polygon2):
    sum1 = calculate_angle_sum(polygon1)
    sum2 = calculate_angle_sum(polygon2)
    if sum1 > sum2:
        return "Triangle has a larger total interior angle sum."
    elif sum1 < sum2:
        return "Quadrilateral has a larger total interior angle sum."
    else:
        return "Both polygons have the same total interior angle sum."

if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, 1)]
    quadrilateral = [(0, 0), (1, 0), (1, 1), (0, 1)]
    
    result = compare_polygons(triangle, quadrilateral)
    print(result)