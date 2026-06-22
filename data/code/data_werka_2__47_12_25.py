def calculate_triangle_area(p1, p2, p3):
    def determinant(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    
    try:
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3]):
            raise ValueError("All coordinates must be integers or floats.")
        return determinant(x1, y1, x2, y2, x3, y3)
    except TypeError:
        raise ValueError("Each vertex must be a tuple of two numbers.")

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    area = calculate_triangle_area(*vertices)
    print(area)