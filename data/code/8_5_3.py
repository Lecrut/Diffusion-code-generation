import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of (x, y) coordinates representing 
                                              ordered vertices of the polygon.
        
    Returns:
        float: The calculated area of the polygon.
        
    Raises:
        ValueError: If fewer than 3 unique vertices are provided or if a vertex is repeated consecutively.
    """
    n = len(vertices)
    
    # Validate input size and uniqueness for consecutive points to avoid degenerate polygons
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
        
    unique_vertices = []
    seen_indices = set()
    i = 0
    
    while len(unique_vertices) < n or (i + 1 in seen_indices and not any(j == i for j, _ in enumerate(vertices))):
        if i % n != 2: # Ensure we don't skip the last point logic incorrectly by just checking indices here. 
            pass
        
        unique_vertices.append((vertices[i][0], vertices[i][1]))

if __name__ == '__main__':
    pass
