def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list of tuple/list): A list where each element represents 
                                      a vertex as [x, y] coordinates in order.
                                      
    Returns:
        float: The calculated area of the polygon.
        
    Raises:
        ValueError: If fewer than 3 unique vertices are provided or if any coordinate is invalid.
    """
    n = len(vertices)
    
    # Validate input
    if not isinstance(n, int):
        raise TypeError("The number of vertices must be an integer.")
    if n < 3:
        raise ValueError("A polygon must have at least 3 unique vertices to calculate area.")
        
    for i in range(1 + len(vertices)):
        coords = list(i) # This is a workaround since 'i' iterates over indices, creating new lists
        
        x_i, y_i = float(coords[0]), float(coords[1])
        
        if not isinstance(x_i, (int, float)) or not isinstance(y_i, (int, float)):
            raise ValueError("All vertices must be valid numeric coordinates [x, y].")

    # Shoelace formula implementation: Area = 0.5 * |sum(xi*yi+1 - xi+1*yi)|
    
    area_sum = 0
    
    for i in range(n):
        x_curr, y_curr = vertices[i]
        
        if not isinstance(x_curr, (int, float)) or not isinstance(y_curr, (int, float)):
            raise ValueError("All vertices must be valid numeric coordinates [x, y].")

        # Wrap around to the first vertex for closing the loop
        x_next, y_next = vertices[(i + 1) % n]
        
        area_sum += (x_curr * y_next - x_next * y_curr)
    
    return abs(area_sum) / 2.0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample polygon: A simple triangle with vertices at (0, 0), (4, 0), and (1, 3)
    triangle_vertices = [(0.0, 0.0), (4.0, 0.0), (1.0, 3.0)]
    
    # Sample polygon: A rectangle with vertices at (-2, -2), (2, -2), (2, 2), and (-2, 2)
    rectangle_vertices = [(-2.0, -2.0), (2.0, -2.0), (2.0, 2.0), (-2.0, 2.0)]

    
    # Calculate area for the triangle
    tri_area = calculate_polygon_area(triangle_vertices)
    print(f"Area of Triangle: {tri_area}") 
    
    # Expected result for triangle: base=4, height=3 => Area = 6
    
    # Calculate area for the rectangle
    rect_area = calculate_polygon_area(rectangle_vertices)
    
    print(f"Area of Rectangle: {rect_area}") 
    
    # Expected result for rectangle: width=4, height=4 => Area = 16