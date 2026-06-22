def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    if not all((isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3])):
        raise ValueError('All coordinates must be numbers.')
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
if __name__ == '__main__':
    vertex_a = (1, 2)
    vertex_b = (4, 5)
    vertex_c = (7, 8)
    try:
        area = calculate_triangle_area(*vertex_a, *vertex_b, *vertex_c)
        print(f'The area of the triangle is: {area}')
    except ValueError as e:
        print(e)