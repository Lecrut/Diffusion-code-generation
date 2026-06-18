import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of (x, y) coordinates representing 
                                             ordered vertices of the polygon.
                                              The list must contain at least 3 points.
                                            
    Returns:
        float: The area of the polygon. If fewer than 3 vertices are provided, returns None.
    
    Raises:
        ValueError: If any vertex is not a tuple of two numeric values or if coordinates 
                   cannot be converted to numbers.
    """
    n = len(vertices)
    if n < 3:
        return None

    try:
        x_coords = [float(v[0]) for v in vertices]
        y_coords = [float(v[1]) for v in vertices]
        
        area = abs(0.5 * sum(x[i + 1 % n] * y[i] - x[i] * y[i + 1 % n] 
                            for i in range(n)))
    except (TypeError, ValueError):
        raise ValueError("All vertices must be tuples of numeric coordinates.")

    return area

if __name__ == '__main__':
    # Sample polygon: a simple triangle with vertices at (0,0), (4,0), and (2,3)
    sample_vertices = [(0.0, 0.0), (4.0, 0.0), (2.0, 3.0)]
    
    area_result = calculate_polygon_area(sample_vertices)
    
    if area_result is not None:
        print(f"Area of the polygon: {area_result}")
        
        # Additional test case for a square
        square_vertices = [(1.0, 1.0), (4.0, 1.0), (4.0, 3.0), (1.0, 3.0)]
        square_area = calculate_polygon_area(square_vertices)
        
        if square_area is not None:
            print(f"Area of the square: {square_area}")
    else:
        print("Invalid polygon vertex count.")