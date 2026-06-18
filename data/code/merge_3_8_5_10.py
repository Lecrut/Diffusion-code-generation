import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple]): A list of tuples representing the coordinates [(x1, y1), (x2, y2), ...].
                                The first and last vertex must be identical to close the shape if not provided.

    Returns:
        float: The area of the polygon as a non-negative number.
    
    Raises:
        ValueError: If fewer than 3 vertices are provided or coordinates are invalid.
    """
    n = len(vertices)
    
    # Ensure at least 3 points to form a polygon
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    for i, (x, y) in enumerate(vertices):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Invalid coordinate type at index {i}. Expected numeric value.")

    # Close the polygon by appending the first vertex to the end if it's not already there
    vertices_with_close = vertices + [vertices[0]]

    area = 0.5 * abs(
        sum(vertices[i][0] * vertices[(i + 1) % len(vertices_with_close)][1] for i in range(len(vertices))) -
        sum(vertices[i][1] * vertices[(i + 1) % len(vertices_with_close)][0] for i in range(len(vertices)))
    )

    return area

if __name__ == '__main__':
    # Sample polygon: a triangle with points (0, 0), (4, 0), and (2, 3)
    sample_vertices = [(0.0, 0.0), (4.0, 0.0), (2.0, 3.0)]

    try:
        area_result = calculate_polygon_area(sample_vertices)
        print(f"Area of the polygon with vertices {sample_vertices}: {area_result}")
        
        # Additional test case: a square defined as [(1,1), (4,1), (4,4), (1,4)]
        sample_square = [(1.0, 1.0), (4.0, 1.0), (4.0, 4.0), (1.0, 4.0)]
        
        area_result_sq = calculate_polygon_area(sample_square)
        print(f"Area of the square with vertices {sample_square}: {area_result_sq}")

    except Exception as e:
        print(f"An error occurred during calculation: {e}")