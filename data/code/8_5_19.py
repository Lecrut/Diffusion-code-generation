import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple]): A list of tuples representing [x, y] coordinates 
                               in order (clockwise or counter-clockwise).
    
    Returns:
        float: The absolute area of the polygon.
    
    Raises:
        ValueError: If fewer than 3 unique vertices are provided.
        TypeError: If input is not a list of tuples with exactly two numeric elements.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    n = len(vertices)
    
    # Validate vertex format and uniqueness check (basic)
    for i, v in enumerate(vertices):
        if not isinstance(v, tuple) or len(v) != 2:
            raise TypeError(f"Vertex {i} must be a tuple of two numbers.")
        try:
            float(v[0])
            float(v[1])
        except (TypeError, ValueError):
            raise TypeError(f"Coordinates at vertex {i} are not numeric.")

    area = 0.5 * abs(
        sum(vertices[i][0] * vertices[(i + 1) % n][1] - 
                    vertices[i][1] * vertices[(i + 1) % n][0]) 
        for i in range(n)
    )
    
    return area

if __name__ == '__main__':
    # Sample polygon: a square with vertices (0,0), (4,0), (4,4), (0,4)
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    
    try:
        area_result = calculate_polygon_area(sample_vertices)
        print(f"Area of the polygon with vertices {sample_vertices}:")
        print(f"{area_result:.2f}")
        
        # Additional test case: a triangle
        sample_triangle = [(10, 5), (30, 7), (40, -8)]
        area_tri = calculate_polygon_area(sample_triangle)
        print(f"\nArea of the triangle with vertices {sample_triangle}:")
        print(f"{area_tri:.2f}")
        
    except Exception as e:
        print(f"An error occurred during calculation: {e}")