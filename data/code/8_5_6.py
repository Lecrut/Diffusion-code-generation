import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of [x, y] coordinates representing 
                                              ordered vertices of the polygon.
                                               The list should not be empty and must have at least 3 points.
    
    Returns:
        float: The area of the polygon.
    
    Raises:
        ValueError: If fewer than 3 unique vertices are provided or if any vertex is None/empty tuple.
    """
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    for i, v in enumerate(vertices):
        if not isinstance(v, (list, tuple)) or len(v) != 2:
            raise ValueError(f"Invalid vertex format at index {i}. Expected [x, y] list/tuple.")
    
    area = 0.5 * abs(sum(
        vertices[i][0] * vertices[(i + 1) % n][1] - 
        vertices[i][1] * vertices[(i + 1) % n][0]
    ) for i in range(n))

    return area

if __name__ == '__main__':
    # Sample polygon: a simple square with side length 4, centered at origin.
    sample_vertices = [
        (2, -2),
        (-2, -2),
        (-2, 2),
        (2, 2)
    ]

    area_result = calculate_polygon_area(sample_vertices)
    
    print(f"Area of polygon with vertices {sample_vertices}:")
    print(f"{area_result}")