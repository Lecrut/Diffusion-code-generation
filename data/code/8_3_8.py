def compute_polygon_area(vertices):
    region_types = {
        'triangle': 3,
        'quadrilateral': 4,
        'pentagon': 5
    }
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    cross_sum = 0
    for i in range(n):
        current_x = vertices[i][0]
        current_y = vertices[i][1]
        next_idx = (i + 1) % n
        next_x = vertices[next_idx][0]
        next_y = vertices[next_idx][1]
        cross_sum += current_x * next_y
        cross_sum -= next_x * current_y
    area = abs(cross_sum) / 2.0
    return area
if __name__ == '__main__':
    regular_hexagon = [(1, 0), (0.5, 0.866025), (-0.5, 0.866025), (-1, 0), (-0.5, -0.866025), (0.5, -0.866025)]
    calculated_area = compute_polygon_area(regular_hexagon)
    print(calculated_area)