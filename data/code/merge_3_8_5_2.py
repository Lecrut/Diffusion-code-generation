import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given a list of vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): A list of (x, y) tuples representing the 
                                              ordered vertices of the polygon.
                                               The first vertex should be connected to 
                                              the last one for closed shape calculation.

    Returns:
        float: The area of the polygon. If fewer than 3 unique vertices are provided, 
               returns 0.0. Negative areas (indicating clockwise order) return positive values.
    
    Raises:
        ValueError: If input is not a list or contains invalid vertex types.
    """
    if len(vertices) < 3:
        return 0.0

    # Validate input format
    for i, v in enumerate(vertices):
        try:
            x = float(v[0])
            y = float(v[1])
        except (TypeError, IndexError, ValueError) as e:
            raise ValueError(f"Invalid vertex at index {i}: expected tuple of two numbers") from e

    n = len(vertices)
    
    # Shoelace formula implementation
    area = 0.5 * abs(sum(
        vertices[i][0] * vertices[(i + 1) % n][1] - 
        vertices[i][1] * vertices[(i + 1) % n][0]
        for i in range(n)
    ))

    return area

if __name__ == '__main__':
    # Sample polygon: a rectangle with vertices (0,0), (4,0), (4,3), (0,3)
    sample_vertices = [(0.0, 0.0), (4.0, 0.0), (4.0, 3.0), (0.0, 3.0)]

    area_result = calculate_polygon_area(sample_vertices)

    print(f"Polygon vertices: {sample_vertices}")
    print(f"Calculated Area: {area_result} square units")