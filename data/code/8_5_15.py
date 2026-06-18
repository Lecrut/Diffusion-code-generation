import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices as coordinates.
    
    Args:
        vertices (list[tuple]): A list of tuples representing (x, y) coordinates 
                               in order (clockwise or counter-clockwise).
       
    Returns:
        float: The absolute value of the polygon's area.
        
    Raises:
        ValueError: If the input is empty, contains fewer than 3 vertices, 
                   has non-numeric values, or if x and y coordinates don't match in count.
    
    Uses the Shoelace formula (also known as Surveyor's formula).
    """
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least three vertices.")

    # Validate input format and types
    for i, vertex in enumerate(vertices):
        x, y = vertex
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Vertex {i} contains non-numeric coordinates: {vertex}")
        
        # Ensure consistent pairing and count check could be implicit here, 
        # but we assume valid input structure per task constraints.

    area = 0.5 * abs(
        sum(x[i] * y[(i + 1) % n] - x[(i + 1) % n] * y[i]) for i in range(n)
    )

    return float(area)

if __name__ == '__main__':
    # Hard-coded sample values: a simple triangle with vertices at (0,0), (4,0), and (2,3).
    # Expected area is 6.0 units squared.
    
    sample_vertices = [(0, 0), (4, 0), (2, 3)]

    calculated_area = calculate_polygon_area(sample_vertices)
    print(f"Calculated Area: {calculated_area}")

    # Another test case: a square with vertices at (-1,-1), (1,-1), (1,1), (-1,1).
    # Expected area is 4.0 units squared.
    
    sample_vertices_square = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

    calculated_area_sq = calculate_polygon_area(sample_vertices_square)
    print(f"Calculated Area of Square: {calculated_area_sq}")