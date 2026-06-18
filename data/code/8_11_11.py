import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): A list of ordered (x, y) tuples representing 
                                             the vertices of the polygon in order (either clockwise or counter-clockwise).
        
    Returns:
        float: The area of the polygon as a non-negative number.
    
    Raises:
        ValueError: If fewer than 3 unique vertices are provided.
        TypeError: If any vertex is not a tuple of two numbers.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    # Validate input types and ensure all points are tuples/lists with exactly two numeric elements
    for i, point in enumerate(vertices):
        if not isinstance(point, (tuple, list)):
            raise TypeError(f"Vertex {i} is not a tuple or list. Expected: ((x, y), ...). Got: {point}")
        try:
            x = float(point[0])
            y = float(point[1])
        except (IndexError, ValueError):
            raise TypeError(f"Invalid coordinates at vertex {i}: {point}. Coordinates must be numeric.")

    n = len(vertices)
    
    # Shoelace formula implementation with floating-point tolerance handling for edge cases
    area_sum = 0.0
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to the first vertex
        
        area_sum += (x1 * y2 - x2 * y1)

    # Take absolute value and divide by 2.0 for final positive area
    raw_area = abs(area_sum / 2.0)

    return round(raw_area, 6)

if __name__ == '__main__':
    # Sample polygon: a rectangle with vertices (0,0), (4,0), (4,3), (0,3)
    sample_vertices = [
        (0.0, 0.0),
        (4.0, 0.0),
        (4.0, 3.0),
        (0.0, 3.0)
    ]

    # Calculate area using the function
    polygon_area = calculate_polygon_area(sample_vertices)

    print(f"Calculated Area: {polygon_area}")
    
    # Additional test case with floating point coordinates
    sample_float_vertices = [
        (1.5, 2.0),
        (3.7, 4.5),
        (6.2, 1.8)
    ]

    float_polygon_area = calculate_polygon_area(sample_float_vertices)
    
    print(f"Calculated Area for Float Polygon: {float_polygon_area}")