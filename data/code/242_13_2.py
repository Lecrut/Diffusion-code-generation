import math
def calculate_area_difference(triangle_sides, quadrilateral_sides):
    a, b, c = triangle_sides
    s = (a + b + c) / 2
    area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
    x1, y1, x2, y2, x3, y3, x4, y4 = quadrilateral_sides
    area_quadrilateral = 0.5 * abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1))
    return abs(area_triangle - area_quadrilateral)
if __name__ == '__main__':
    triangle = (3, 4, 5)
    quadrilateral = (0, 0, 2, 4, 6, 4, 8, 0)
    difference = calculate_area_difference(triangle, quadrilateral)
    print(difference)