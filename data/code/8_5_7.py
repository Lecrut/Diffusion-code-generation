def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple]): List of (x, y) coordinates representing vertices in order.
        
    Returns:
        float: The calculated area of the polygon.
    """
    n = len(vertices)
    if n < 3:
        return 0.0

    area = 0.5 * abs(
        sum(x[i] * y[i+1] - x[i+1] * y[i] 
                 for i in range(n)) + vertices[0][0]*vertices[n-1][1] - vertices[0][1]*vertices[n-1][0])

    return area

if __name__ == '__main__':
    # Sample polygon defined as a rectangle with known positive and negative coordinates
    sample_vertices = [
        (0, 0), 
        (4, 0), 
        (4, -3), 
        (-1, -3)
    ]

    area_value = calculate_polygon_area(sample_vertices)
    
    # Output the result to verify functionality without user interaction
    print(f"The area of the polygon is: {area_value}")