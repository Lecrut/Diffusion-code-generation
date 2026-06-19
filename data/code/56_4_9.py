import math

def calculate_angle_sum(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError('A polygon must have at least 3 vertices.')
    angle_sum = 0.0
    for i in range(n):
        a, b, c = (vertices[i], vertices[(i + 1) % n], vertices[(i + 2) % n])
        v1 = (b[0] - a[0], b[1] - a[1])
        v2 = (c[0] - b[0], c[1] - b[1])
        v3 = (a[0] - c[0], a[1] - c[1])
        mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
        mag_v3 = math.sqrt(v3[0] ** 2 + v3[1] ** 2)
        if mag_v1 == 0 or mag_v2 == 0 or mag_v3 == 0:
            continue
        dot_product1 = v1[0] * v2[0] + v1[1] * v2[1]
        dot_product2 = v2[0] * v3[0] + v2[1] * v3[1]
        try:
            angle1 = math.acos(dot_product1 / (mag_v1 * mag_v2))
            angle2 = math.acos(dot_product2 / (mag_v2 * mag_v3))
            angle_sum += angle1 + angle2
        except ValueError:
            return float('inf')
    return angle_sum

def compare_polygons(triangle, quadrilateral):
    try:
        triangle_angle_sum = calculate_angle_sum(triangle)
        quadrilateral_angle_sum = calculate_angle_sum(quadrilateral)
        if triangle_angle_sum > quadrilateral_angle_sum:
            return 'Triangle has a larger total interior angle sum.'
        elif triangle_angle_sum < quadrilateral_angle_sum:
            return 'Quadrilateral has a larger total interior angle sum.'
        else:
            return 'Both polygons have the same total interior angle sum.'
    except ValueError as e:
        return str(e)
if __name__ == '__main__':
    triangle = [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)]
    quadrilateral = [(0, 0), (2, 0), (2, 2), (0, 2)]
    result = compare_polygons(triangle, quadrilateral)
    print(result)