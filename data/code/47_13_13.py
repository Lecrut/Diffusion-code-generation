def validate_point(point):
    if not isinstance(point, tuple) or len(point) != 2:
        raise ValueError("Each point must be a tuple of two numbers.")
    x, y = point
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Coordinates must be numeric values.")

def triangle_area(p1, p2, p3):
    validate_point(p1)
    validate_point(p2)
    validate_point(p3)
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    area = triangle_area(*vertices)
    print(f"Area of the triangle: {area:.2f}")