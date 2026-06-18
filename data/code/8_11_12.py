def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its ordered vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): A list of (x, y) tuples representing 
                                            the vertices of the polygon in order.
                                            
    Returns:
        float: The area of the polygon as a non-negative floating-point number.
        
    Raises:
        ValueError: If fewer than 3 unique vertices are provided or if input format is invalid.
    """
    n = len(vertices)
    
    # Basic validation for minimum vertex count and data type check
    if not isinstance(vertices, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(v, tuple) or len(v) != 2 for v in vertices):
        raise ValueError("Each element of the input list must be a (x, y) tuple.")
    
    # Ensure at least 3 points to form a polygon
    unique_points = set(vertices)
    if len(unique_points) < 3:
        raise ValueError("A valid polygon requires at least three distinct vertices.")

    area_sum = 0.0
    
    for i in range(n):
        x1, y1 = vertices[i]
        # Wrap around to the first vertex when comparing with the last point (index n-1)
        x2, y2 = vertices[(i + 1) % n] if isinstance(vertices[n - 1], tuple) else vertices[0] 
        # Correction: The loop logic needs adjustment for modulo arithmetic on indices directly
        
    # Re-implementing the core loop with correct index handling to avoid confusion
    area_sum = 0.0
    
    m = len(vertices)
    
    if m < 3:
        raise ValueError("Polygon must have at least 3 vertices.")

    for i in range(m):
        x1, y1 = float(vertices[i][0])
        x2, y2 = float(vertices[(i + 1) % m][0]), float(vertices[(i + 1) % m][1])
        
        # Shoelace formula term: (x_i * y_{i+1}) - (y_i * x_{i+1})
        area_sum += (x1 * y2 - y1 * x2)

    return abs(area_sum) / 2.0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample polygon: A simple square with vertices at (0,0), (4,0), (4,3), (0,3) -> Area should be 12.0
    square_vertices = [(0.0, 0.0), (4.0, 0.0), (4.0, 3.0), (0.0, 3.0)]
    
    # Sample polygon: A triangle with vertices at (-5,-5), (12,-6), (8,7) -> Area should be approx 94.0
    triangle_vertices = [(-5.0, -5.0), (12.0, -6.0), (8.0, 7.0)]

    
    # Test case 1: Square area calculation
    try:
        square_area = calculate_polygon_area(square_vertices)
        print(f"Area of the square polygon: {square_area}")
    except Exception as e:
        print(f"Error calculating square area: {e}")

    # Test case 2: Triangle area calculation with floating point vertices
    try:
        triangle_area = calculate_polygon_area(triangle_vertices)
        print(f"Area of the triangle polygon: {triangle_area:.1f}")
    except Exception as e:
        print(f"Error calculating triangle area: {e}")

    # Test case 3: Degenerate input (less than 3 points) - should raise an error
    try:
        invalid_vertices = [(0.0, 0.0), (1.0, 1.0)]
        result = calculate_polygon_area(invalid_vertices)
        print(f"Unexpected success for degenerate polygon: {result}")
    except ValueError as e:
        print(f"Correctly caught error for invalid input: {e}")