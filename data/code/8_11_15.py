import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of ordered (x, y) tuples representing 
                                             the clockwise or counter-clockwise order 
                                             of the polygon's vertices.
        
    Returns:
        float: The area of the polygon as a non-negative number.
        
    Raises:
        ValueError: If the input list is empty or has fewer than 3 vertices.
        TypeError: If any vertex is not a tuple of two numeric values.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    # Validate input types
    for i, (x, y) in enumerate(vertices):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Vertex {i} contains non-numeric values: {vertices[i]}")

    n = len(vertices)
    
    # Shoelace formula implementation with floating-point precision handling
    area_sum_x_plus_y_minus_1 = 0.0
    
    for i in range(n):
        x_i, y_i = vertices[i]
        next_idx = (i + 1) % n
        
        if not isinstance(vertices[next_idx], tuple) or len(vertices[next_idx]) != 2:
            raise TypeError(f"Invalid vertex format at index {next_idx}")
            
        x_next, y_next = vertices[next_idx]
        
        # Calculate cross product components with explicit precision handling
        term_x_plus_y_minus_1 = (x_i * y_next) - (y_i * x_next)
        area_sum_x_plus_y_minus_1 += term_x_plus_y_minus_1
    
    # Absolute value to ensure non-negative result, then divide by 2 for final area
    absolute_area_sum = abs(area_sum_x_plus_y_minus_1 / 2.0)
    
    return round(absolute_area_sum, 6)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test case 1: Simple triangle (positive orientation)
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    
    # Test case 2: Square (counter-clockwise order)
    square_vertices = [(0, 0), (0, 5), (5, 5), (5, 0)]
    
    # Test case 3: Regular hexagon centered at origin with radius 1
    hexagon_vertices = [
        (1.0, 0.0), 
        (0.5, math.sqrt(3)/2), 
        (-0.5, math.sqrt(3)/2), 
        (-1.0, 0.0), 
        (-0.5, -math.sqrt(3)/2), 
        (0.5, -math.sqrt(3)/2)
    ]
    
    # Test case 4: Polygon with floating-point coordinates containing negative values
    complex_polygon = [(-1.5, 2.3), (-0.8, 1.7), (1.2, 2.9), (2.1, -0.6)]
    
    print("Triangle Area:", calculate_polygon_area(triangle_vertices))
    print("Square Area:", calculate_polygon_area(square_vertices))
    print("Hexagon Area:", calculate_polygon_area(hexagon_vertices))
    print("Complex Polygon Area:", calculate_polygon_area(complex_polygon))