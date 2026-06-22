def calculate_triangle_area(p1, p2, p3):
    try:
        if not (isinstance(p1, tuple) and isinstance(p2, tuple) and isinstance(p3, tuple)):
            raise ValueError("All vertices must be tuples.")
        if not (len(p1) == 2 and len(p2) == 2 and len(p3) == 2):
            raise ValueError("Each vertex must have exactly two coordinates.")
        
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        if not (isinstance(x1, (int, float)) and isinstance(y1, (int, float))
                and isinstance(x2, (int, float)) and isinstance(y2, (int, float))
                and isinstance(x3, (int, float)) and isinstance(y3, (int, float))):
            raise ValueError("Coordinates must be numeric values.")
        
        area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
        return area
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    area = calculate_triangle_area(*vertices)
    print(f"Area of the triangle: {area:.2f}")