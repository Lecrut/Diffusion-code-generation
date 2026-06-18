import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of [x, y] coordinates representing 
                                              ordered vertices of the polygon.
                                               The list must contain at least 3 points.
    
    Returns:
        float: The area of the polygon. If fewer than 3 vertices are provided, returns None.
               Raises ValueError if any vertex is not a tuple or has incorrect length.
    """
    n = len(vertices)
    if n < 3:
        return None
    
    # Validate input format
    for i, v in enumerate(vertices):
        if not isinstance(v, (list, tuple)) or len(v) != 2:
            raise ValueError(f"Vertex {i} must be a [x, y] coordinate pair.")
    
    area = 0.0
    
    # Shoelace formula implementation
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        
        cross_product = (x1 * y2 - x2 * y1)
        area += cross_product
    
    return abs(area / 2.0)

if __name__ == '__main__':
    # Sample polygon: a square with vertices at (0,0), (4,0), (4,4), (0,4)
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    
    area_result = calculate_polygon_area(sample_vertices)
    
    print(f"Area of polygon with vertices {sample_vertices}:")
    if area_result is not None:
        print(f"{area_result:.2f}")
    else:
        print("Invalid number of vertices.")

    # Sample triangle for additional verification
    sample_triangle = [(0, 0), (5, 0), (0, 3)]
    
    triangle_area = calculate_polygon_area(sample_triangle)
    
    print(f"\nArea of polygon with vertices {sample_triangle}:")
    if triangle_area is not None:
        print(f"{triangle_area:.2f}")