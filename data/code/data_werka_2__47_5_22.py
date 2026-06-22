def calculate_area(x1, y1, x2, y2, x3, y3):
    if not all((isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3])):
        raise ValueError('All coordinates must be numbers.')
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    try:
        area = calculate_area(*vertices[0], *vertices[1], *vertices[2])
        print(area)
    except ValueError as e:
        print(e)