def calculate_triangle_area(p1, p2, p3):
    try:
        x1, y1 = map(float, p1)
        x2, y2 = map(float, p2)
        x3, y3 = map(float, p3)
        
        if any(coord <= 0 for coord in (x1, y1, x2, y2, x3, y3)):
            raise ValueError("All coordinates must be positive values.")
        
        area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
        return area
    
    except (TypeError, ValueError) as e:
        raise ValueError("Invalid input. Please enter valid numeric coordinates.") from e

if __name__ == '__main__':
    try:
        vertices = [(3, 4), (6, 8), (9, 12)]
        area = calculate_triangle_area(*vertices)
        print(f"Area of the triangle: {area:.2f}")
    except ValueError as e:
        print(e)