def triangle_area(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3]):
        raise ValueError('All coordinates must be numbers.')
    
    def determinant(xa, ya, xb, yb, xc, yc):
        return xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)
    
    return abs(determinant(x1, y1, x2, y2, x3, y3)) / 2.0

if __name__ == '__main__':
    try:
        area = triangle_area(0, 0, 4, 0, 2, 3)
        print(area)
    except ValueError as e:
        print(e)