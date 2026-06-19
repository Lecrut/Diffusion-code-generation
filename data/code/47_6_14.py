def validate_coordinates(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(c, (int, float)) for c in [x1, y1, x2, y2, x3, y3]):
        raise ValueError("All coordinates must be numbers.")
    if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x3, y3) == (x1, y1):
        raise ValueError("Vertices cannot be the same point.")

def triangle_area(x1, y1, x2, y2, x3, y3):
    validate_coordinates(x1, y1, x2, y2, x3, y3)
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    x1, y1 = (0, 0)
    x2, y2 = (4, 0)
    x3, y3 = (2, 3)
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    print(area)