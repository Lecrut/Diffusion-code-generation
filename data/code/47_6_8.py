def triangle_area(x1, y1, x2, y2, x3, y3):
    term1 = x1 * (y2 - y3)
    term2 = x2 * (y3 - y1)
    term3 = x3 * (y1 - y2)
    return abs((term1 + term2 + term3) / 2.0)
if __name__ == '__main__':
    vertex1 = (1, 1)
    vertex2 = (4, 5)
    vertex3 = (7, 2)
    x1, y1 = vertex1
    x2, y2 = vertex2
    x3, y3 = vertex3
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    print(area)