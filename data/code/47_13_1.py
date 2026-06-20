def triangle_area(v1, v2, v3):
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    return area

if __name__ == '__main__':
    vertices = ((0, 0), (4, 0), (0, 3))
    result = triangle_area(*vertices)
    print(result)