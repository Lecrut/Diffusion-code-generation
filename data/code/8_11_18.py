import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given ordered (x, y) vertex tuples using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of n >= 3 ordered (x, y) coordinates representing 
                                             the vertices of the polygon in order (clockwise or counter-clockwise).
    
    Returns:
        float: The area of the polygon as a non-negative number.
    
    Raises:
        ValueError: If fewer than 3 vertices are provided.
        TypeError: If any vertex is not a tuple of two numeric values.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    n = len(vertices)
    
    # Validate input types and ensure all coordinates are numbers
    for i, (x, y) in enumerate(vertices):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Vertex {i} contains non-numeric coordinate values.")

    area = 0.0
    
    # Shoelace formula implementation: Area = 0.5 * |sum(xi*yi+1 - xi+1*yi)|
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        
        # Add to the cross product sum with high precision arithmetic handling via standard floats (IEEE 754 double precision is sufficient for most geometric applications unless extreme coordinates are used)
        area += (x_i * y_next - x_next * y_i)

    return abs(area) / 2.0

if __name__ == '__main__':
    # Sample polygon: Square with vertices at (1,1), (4,1), (4,4), (1,4)
    square_vertices = [(1, 1), (4, 1), (4, 4), (1, 4)]
    
    # Another sample: Pentagon approximated by specific coordinates with floating points
    pentagon_vertices = [
        (0.5, 2.3), 
        (3.7, -0.8), 
        (-2.9, -1.6), 
        (-3.4, 2.9), 
        (0.5, 2.3) # Closing the loop implicitly handled by formula
    ]

    print("Area of square:", calculate_polygon_area(square_vertices))
    print("Area of pentagon:", calculate_polygon_area(pentagon_vertices))
    
    # Test with floating point coordinates that might introduce slight inaccuracies if not handled correctly
    float_poly = [(0.1, 0.2), (0.3, 0.4), (0.5, 0.6)]
    print("Area of small float polygon:", calculate_polygon_area(float_poly))