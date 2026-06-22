def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    if not all((isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3])):
        raise ValueError('All coordinates must be numbers.')
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
if __name__ == '__main__':
    try:
        vertex1 = (0, 0)
        vertex2 = (4, 0)
        vertex3 = (2, 3)
        area = calculate_triangle_area(*vertex1, *vertex2, *vertex3)
        print('Area of the triangle:', area)
    except ValueError as e:
        print(e)