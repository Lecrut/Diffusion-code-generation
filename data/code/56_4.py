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
        v1 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
        v2 = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
        v3 = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)
        if v1 == 0 or v2 == 0 or v3 == 0:
            continue
        try:
            cosine_angle = (v1**2 + v3**2 - v2**2) / (2 * v1 * v3)
            cosine_angle = max(-1.0, min(1.0, cosine_angle))
            angle = math.acos(cosine_angle)
            angle_sum += angle
        except ZeroDivisionError:
            continue
    return angle_sum
def solve():
    triangle_vertices = [
        (0, 0),
        (4, 0),
        (0, 3)
    ]
    quadrilateral_vertices = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
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