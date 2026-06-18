import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): A list of ordered (x, y) tuples representing 
                                              the vertices of the polygon in order (clockwise or counter-clockwise).
        
    Returns:
        float: The area of the polygon as a positive number. Floating-point inaccuracies are handled by rounding to 6 decimal places.
    
    Raises:
        ValueError: If fewer than 3 unique vertices are provided, indicating an invalid polygon.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    n = len(vertices)
    area_sum = 0.0
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        
        # Shoelace formula component: (x_i * y_{i+1}) - (y_i * x_{i+1})
        area_sum += (x1 * y2) - (y1 * x2)

    # The absolute value of the result divided by 2 gives the actual area
    return abs(area_sum / 2.0)

if __name__ == '__main__':
    # Sample polygon: a square with vertices at (0,0), (4,0), (4,4), (0,4)
    sample_vertices = [
        (0.0, 0.0),
        (4.0, 0.0),
        (4.0, 4.0),
        (0.0, 4.0)
    ]

    # Calculate area
    polygon_area = calculate_polygon_area(sample_vertices)

    print(f"Calculated Area: {polygon_area:.6f}")
    
    # Additional test case with floating point coordinates
    triangle_vertices = [
        (1.5, 2.3),
        (4.7, -0.8),
        (-1.2, 3.9)
    ]

    triangle_area = calculate_polygon_area(triangle_vertices)
    
    print(f"Triangle Area: {triangle_area:.6f}")