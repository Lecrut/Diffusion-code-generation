def calculate_polygon_area(vertices):
    count = len(vertices)
    if count < 3:
        return 0.0
    cross_sum = 0.0
    for index in range(count):
        next_index = (index + 1) % count
        current_x = vertices[index][0]
        current_y = vertices[index][1]
        next_x = vertices[next_index][0]
        next_y = vertices[next_index][1]
        term_1 = current_x * next_y
        term_2 = next_x * current_y
        cross_sum += term_1
        cross_sum -= term_2
    magnitude = abs(cross_sum)
    return magnitude / 2.0

if __name__ == '__main__':
    irregular_polygon = [(-2, 1), (3, 4), (5, -2), (1, -5), (-3, -1)]
    area_value = calculate_polygon_area(irregular_polygon)
    print(area_value)
    triangle_test = [(1, 1), (4, 5), (7, 1)]
    triangle_area = calculate_polygon_area(triangle_test)
    print(triangle_area)