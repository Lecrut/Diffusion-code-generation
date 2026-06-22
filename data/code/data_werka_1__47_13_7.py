def calculate_triangle_area(p1, p2, p3):
    try:
        x1, y1 = map(float, p1)
        x2, y2 = map(float, p2)
        x3, y3 = map(float, p3)
        
        if not all(isinstance(coord, float) for coord in [x1, y1, x2, y2, x3, y3]):
            raise ValueError("All coordinates must be numeric.")
        
        area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
        if area < 0:
            raise ValueError("Invalid triangle vertices provided.")
        
        return area
    except ValueError as e:
        raise ValueError(f"Error: {e}")

if __name__ == '__main__':
    try:
        vertices = [(0, 0), (4, 0), (2, 3)]
        area = calculate_triangle_area(*vertices)
        print(f"Area of the triangle: {area:.2f}")
    except ValueError as e:
        print(e)