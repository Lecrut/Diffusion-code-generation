import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices as [x, y] pairs using
    the Shoelace formula (Surveyor's formula).

    Args:
        vertices (list[list[float]]): A list of [x, y] coordinates representing 
                                     the vertices of the polygon in order.
    
    Returns:
        float: The area of the polygon. Negative values are returned if the
               vertex order is clockwise; absolute value represents magnitude.

    Raises:
        ValueError: If fewer than 3 unique vertices are provided.
    """
    n = len(vertices)
    # Ensure at least a triangle (3 points) to define an area
    if n < 3 or any(len(point) != 2 for point in vertices):
        raise ValueError("Polygon must have at least 3 valid [x, y] vertex pairs.")

    total_area = 0.0
    
    # Apply Shoelace formula: Area = |sum((x_i * y_{i+1} - x_{i+1} * y_i))| / 2
    for i in range(n):
        px, py = vertices[i]
        next_x, next_y = vertices[(i + 1) % n]  # Wrap around to the first point
        
        cross_product_term = (px * next_y) - (next_x * py)
        total_area += cross_product_term

    return abs(total_area / 2.0)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Sample polygon: Triangle with vertices at [(1, 3), (-4, -5), (6, -2)]
    triangle_vertices = [[1, 3], [-4, -5], [6, -2]]
    
    # Expected area calculation check 
    expected_area_triangle = abs(
        ((1 * -5) + (-4 * -2) + (6 * 3)) - ((-5 * -4) + (6 * -5) + (1 * -2))
    ) / 2.0
    
    # Sample polygon: Quadrilateral with vertices at [(0, 0), (8, 0), (9, 7), (3, 7)]
    quadrangle_vertices = [[0, 0], [8, 0], [9, 7], [3, 7]]

    # Calculate areas for samples
    area_triangle = calculate_polygon_area(triangle_vertices)
    area_quadrangle = calculate_polygon_area(quadrangle_vertices)
    
    print(f"Area of the triangle: {area_triangle}")
    print(f"Expected area calculation result (manual check): {expected_area_triangle}")
    print(f"Match for triangle: {abs(area_triangle - expected_area_triangle) < 1e-6}")
    print()
    print(f"Area of the quadrilateral: {area_quadrangle}")

    # Additional validation test case with a rectangle [(0,0), (5,0), (5,4), (0,4)] -> Area should be 20.0
    rect_vertices = [[0, 0], [5, 0], [5, 4], [0, 4]]
    area_rectangle = calculate_polygon_area(rect_vertices)
    print(f"Area of the rectangle: {area_rectangle}")